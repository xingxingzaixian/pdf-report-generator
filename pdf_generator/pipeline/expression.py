"""Sandboxed expression evaluator for pipeline operations."""

import ast
import operator
from typing import Any, Dict, Union

import pandas as pd


class _PandasSafeTransformer(ast.NodeTransformer):
    """Rewrite `and`/`or`/`not` to `&`/`|`/`~` so they work with pandas Series."""

    def visit_BoolOp(self, node: ast.BoolOp) -> ast.BinOp:
        self.generic_visit(node)
        op_map = {ast.And: ast.BitAnd, ast.Or: ast.BitOr}
        bin_op = op_map[type(node.op)]()
        result = ast.BinOp(left=node.values[0], op=bin_op, right=node.values[1])
        for val in node.values[2:]:
            result = ast.BinOp(left=result, op=bin_op, right=val)
        return ast.copy_location(result, node)

    def visit_UnaryOp(self, node: ast.UnaryOp) -> ast.UnaryOp:
        self.generic_visit(node)
        if isinstance(node.op, ast.Not):
            return ast.copy_location(
                ast.UnaryOp(op=ast.Invert(), operand=node.operand), node
            )
        return node


def _series_safe_builtin(fn):
    """Wrap a builtin so it works when given pandas Series arguments."""

    def wrapper(*args, **kwargs):
        if args and any(isinstance(a, pd.Series) for a in args):
            scalar_args = []
            for a in args:
                if isinstance(a, pd.Series):
                    scalar_args.append(a.max() if a.dtype != object else a.iloc[0])
                else:
                    scalar_args.append(a)
            return fn(*scalar_args, **kwargs)
        return fn(*args, **kwargs)

    return wrapper


class ExpressionEvaluator:
    """Evaluate simple expressions in a sandboxed environment.

    Supports: arithmetic, comparison, logical operators, basic builtins.
    Blocks: import, exec, eval, file/network access.
    """

    # Allowed operators for comparison
    COMPARE_OPS = {
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Gt: operator.gt,
        ast.GtE: operator.ge,
    }

    # Allowed binary operators
    BINARY_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    # Allowed unary operators
    UNARY_OPS = {
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    # Allowed built-in functions (wrapped for pandas Series safety)
    ALLOWED_BUILTINS = {
        "abs": _series_safe_builtin(abs),
        "len": len,
        "max": _series_safe_builtin(max),
        "min": _series_safe_builtin(min),
        "round": round,
        "sum": sum,
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
    }

    def evaluate(
        self, expression: str, context: Union[pd.DataFrame, Dict[str, Any]]
    ) -> Any:
        """Evaluate an expression safely.

        Args:
            expression: The expression string to evaluate
            context: DataFrame (for column references) or dict of variables

        Returns:
            Evaluation result. For DataFrame contexts with boolean expressions,
            returns a boolean Series suitable for filtering.

        Raises:
            ValueError: If the expression contains blocked operations
        """
        try:
            tree = ast.parse(expression, mode="eval")
        except SyntaxError as e:
            raise ValueError(f"Invalid expression syntax: {e}") from e

        # Transform `and`/`or`/`not` to `&`/`|`/`~` for pandas compatibility
        tree = _PandasSafeTransformer().visit(tree)
        ast.fix_missing_locations(tree)

        # Security check: scan for blocked operations
        self._check_security(tree)

        # Build evaluation namespace
        namespace = {"__builtins__": {}}
        namespace.update(self.ALLOWED_BUILTINS)

        # Add column references if context is a DataFrame
        if isinstance(context, pd.DataFrame):
            for col in context.columns:
                namespace[col] = context[col]

        # Add dict values if context is a dict
        if isinstance(context, dict):
            namespace.update(context)

        # Evaluate
        try:
            code = compile(tree, "<expression>", "eval")
            result = eval(code, namespace)
            return result
        except NameError as e:
            raise ValueError(f"Unknown variable in expression: {e}") from e
        except Exception as e:
            raise ValueError(f"Expression evaluation failed: {e}") from e

    def _check_security(self, tree: ast.AST) -> None:
        """Check that the AST doesn't contain blocked operations."""
        for node in ast.walk(tree):
            # Block imports
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                raise ValueError("Import statements are not allowed in expressions")

            # Block function calls to dangerous builtins
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ("exec", "eval", "compile", "open", "__import__"):
                        raise ValueError(
                            f"Call to '{node.func.id}' is not allowed in expressions"
                        )

            # Block attribute access that could reach dangerous methods
            if isinstance(node, ast.Attribute):
                if node.attr.startswith("_"):
                    raise ValueError(
                        f"Private attribute access '{node.attr}' is not allowed"
                    )
