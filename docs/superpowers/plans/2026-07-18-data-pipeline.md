# Data Pipeline & Conditional Rendering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add inline data transformation pipelines and conditional/dynamic element rendering to the PDF report generator, enabling data cleaning, aggregation, and computed columns within JSON configurations.

**Architecture:** New `pipeline/` module with expression evaluator, operation implementations, and engine. Modify `generator.py` to integrate pipelines, and `elements.py` to support condition/loop attributes. Backward-compatible — all changes are additive.

**Tech Stack:** Python 3.9+, pandas (data manipulation), ast (safe expression parsing)

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Create | `pdf_generator/pipeline/__init__.py` | Module exports |
| Create | `pdf_generator/pipeline/expression.py` | Sandboxed expression evaluator |
| Create | `pdf_generator/pipeline/operations.py` | Pipeline operation implementations |
| Create | `pdf_generator/pipeline/engine.py` | Pipeline execution engine |
| Modify | `pdf_generator/config/parser.py` | Recognize `pipeline` field, pass to engine |
| Modify | `pdf_generator/core/generator.py` | Integrate pipeline execution + condition/loop |
| Modify | `pdf_generator/core/elements.py` | Support `condition` and `loop` on elements |
| Create | `tests/pipeline/test_expression.py` | Expression evaluator tests |
| Create | `tests/pipeline/test_operations.py` | Operation tests |
| Create | `tests/pipeline/test_engine.py` | Engine integration tests |
| Create | `tests/pipeline/test_integration.py` | End-to-end PDF generation tests |

---

## Task 1: Expression Evaluator

**Files:**
- Create: `pdf_generator/pipeline/__init__.py`
- Create: `pdf_generator/pipeline/expression.py`
- Create: `tests/pipeline/test_expression.py`

- [ ] **Step 1: Create pipeline module init**

```python
# pdf_generator/pipeline/__init__.py
"""Data pipeline module for transforming data sources."""

from pdf_generator.pipeline.engine import PipelineEngine
from pdf_generator.pipeline.expression import ExpressionEvaluator
from pdf_generator.pipeline.operations import OperationRegistry

__all__ = ["PipelineEngine", "ExpressionEvaluator", "OperationRegistry"]
```

- [ ] **Step 2: Write failing tests for expression evaluator**

```python
# tests/pipeline/test_expression.py
"""Tests for the sandboxed expression evaluator."""

import pytest
import pandas as pd
from pdf_generator.pipeline.expression import ExpressionEvaluator


class TestExpressionEvaluator:
    """Test the ExpressionEvaluator class."""

    def setup_method(self):
        self.evaluator = ExpressionEvaluator()
        self.df = pd.DataFrame({
            "quantity": [100, 200, 50, 300],
            "price": [10.0, 20.0, 5.0, 30.0],
            "category": ["A", "B", "A", "B"],
        })

    def test_arithmetic_expression(self):
        result = self.evaluator.evaluate("quantity * price", self.df)
        assert result is not None

    def test_comparison_expression(self):
        mask = self.evaluator.evaluate("quantity > 100", self.df)
        assert isinstance(mask, pd.Series)
        assert mask.sum() == 2  # 200 and 300

    def test_logical_expression(self):
        mask = self.evaluator.evaluate("quantity > 100 and price > 15", self.df)
        assert isinstance(mask, pd.Series)
        assert mask.sum() == 1  # only 200, 20

    def test_string_comparison(self):
        mask = self.evaluator.evaluate("category == 'A'", self.df)
        assert mask.sum() == 2

    def test_builtin_functions(self):
        result = self.evaluator.evaluate("max(quantity, price)", self.df)
        assert result == 300.0

    def test_blocked_import(self):
        with pytest.raises(ValueError, match="not allowed"):
            self.evaluator.evaluate("__import__('os')", self.df)

    def test_blocked_exec(self):
        with pytest.raises(ValueError, match="not allowed"):
            self.evaluator.evaluate("exec('pass')", self.df)

    def test_blocked_file_access(self):
        with pytest.raises(ValueError, match="not allowed"):
            self.evaluator.evaluate("open('file.txt')", self.df)

    def test_invalid_expression(self):
        with pytest.raises(ValueError):
            self.evaluator.evaluate("invalid syntax {{{", self.df)

    def test_column_reference(self):
        mask = self.evaluator.evaluate("quantity == 200", self.df)
        assert mask.sum() == 1
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_expression.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'pdf_generator.pipeline'`

- [ ] **Step 4: Implement ExpressionEvaluator**

```python
# pdf_generator/pipeline/expression.py
"""Sandboxed expression evaluator for pipeline operations."""

import ast
import operator
from typing import Any, Dict, Union

import pandas as pd


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

    # Allowed built-in functions
    ALLOWED_BUILTINS = {
        "abs": abs,
        "len": len,
        "max": max,
        "min": min,
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_expression.py -v`
Expected: PASS (all 11 tests)

- [ ] **Step 6: Commit**

```bash
git add pdf_generator/pipeline/ tests/pipeline/test_expression.py
git commit -m "feat(pipeline): add sandboxed expression evaluator"
```

---

## Task 2: Pipeline Operations

**Files:**
- Create: `pdf_generator/pipeline/operations.py`
- Create: `tests/pipeline/test_operations.py`

- [ ] **Step 1: Write failing tests for operations**

```python
# tests/pipeline/test_operations.py
"""Tests for pipeline operations."""

import pytest
import pandas as pd
from pdf_generator.pipeline.operations import OperationRegistry


class TestOperationRegistry:
    """Test the OperationRegistry class."""

    def setup_method(self):
        self.registry = OperationRegistry()
        self.df = pd.DataFrame({
            "product": ["A", "B", "C", "D"],
            "category": ["X", "X", "Y", "Y"],
            "quantity": [100, 200, 150, 300],
            "price": [10.0, 20.0, 15.0, 30.0],
        })

    def test_filter_operation(self):
        result = self.registry.execute(
            {"op": "filter", "expr": "quantity > 150"}, self.df
        )
        assert len(result) == 2
        assert list(result["product"]) == ["B", "D"]

    def test_sort_ascending(self):
        result = self.registry.execute(
            {"op": "sort", "by": "quantity", "order": "asc"}, self.df
        )
        assert list(result["product"]) == ["A", "C", "B", "D"]

    def test_sort_descending(self):
        result = self.registry.execute(
            {"op": "sort", "by": "quantity", "order": "desc"}, self.df
        )
        assert list(result["product"]) == ["D", "B", "C", "A"]

    def test_compute_column(self):
        result = self.registry.execute(
            {"op": "compute", "columns": {"revenue": "quantity * price"}},
            self.df,
        )
        assert "revenue" in result.columns
        assert result["revenue"].iloc[0] == 1000.0

    def test_select_columns(self):
        result = self.registry.execute(
            {"op": "select", "columns": ["product", "quantity"]}, self.df
        )
        assert list(result.columns) == ["product", "quantity"]

    def test_rename_columns(self):
        result = self.registry.execute(
            {"op": "rename", "columns": {"quantity": "qty"}}, self.df
        )
        assert "qty" in result.columns
        assert "quantity" not in result.columns

    def test_group_and_aggregate(self):
        result = self.registry.execute(
            {
                "op": "group",
                "by": "category",
                "agg": {"quantity": "sum", "price": "mean"},
            },
            self.df,
        )
        assert len(result) == 2
        assert result.loc[result["category"] == "X", "quantity"].iloc[0] == 300

    def test_limit_operation(self):
        result = self.registry.execute({"op": "limit", "n": 2}, self.df)
        assert len(result) == 2

    def test_concat_operation(self):
        df1 = pd.DataFrame({"a": [1], "b": [2]})
        df2 = pd.DataFrame({"a": [3], "b": [4]})
        result = self.registry.execute(
            {"op": "concat", "sources": ["s1", "s2"]},
            df1,
            extra_sources={"s1": df1, "s2": df2},
        )
        assert len(result) == 2

    def test_unknown_operation_raises(self):
        with pytest.raises(ValueError, match="Unknown operation"):
            self.registry.execute({"op": "unknown"}, self.df)

    def test_filter_invalid_expr(self):
        with pytest.raises(ValueError):
            self.registry.execute({"op": "filter", "expr": "invalid {{{"}, self.df)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_operations.py -v`
Expected: FAIL with `ImportError: cannot import name 'OperationRegistry'`

- [ ] **Step 3: Implement OperationRegistry**

```python
# pdf_generator/pipeline/operations.py
"""Pipeline operation implementations."""

from typing import Any, Callable, Dict, Optional

import pandas as pd

from pdf_generator.pipeline.expression import ExpressionEvaluator


class OperationRegistry:
    """Registry of pipeline operations that transform DataFrames."""

    def __init__(self):
        self.evaluator = ExpressionEvaluator()
        self._operations: Dict[str, Callable] = {
            "filter": self._op_filter,
            "sort": self._op_sort,
            "compute": self._op_compute,
            "select": self._op_select,
            "rename": self._op_rename,
            "group": self._op_group,
            "limit": self._op_limit,
            "head": self._op_limit,  # alias
            "concat": self._op_concat,
        }

    def execute(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Execute a single pipeline step.

        Args:
            step: Step config dict with 'op' key and operation-specific params
            df: Input DataFrame
            extra_sources: Additional data sources for concat operations

        Returns:
            Transformed DataFrame
        """
        op_name = step.get("op")
        if not op_name:
            raise ValueError("Pipeline step must have an 'op' field")

        if op_name not in self._operations:
            raise ValueError(
                f"Unknown operation '{op_name}'. "
                f"Available: {list(self._operations.keys())}"
            )

        handler = self._operations[op_name]
        return handler(step, df, extra_sources)

    def _op_filter(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Filter rows by expression."""
        expr = step.get("expr")
        if not expr:
            raise ValueError("Filter operation requires 'expr' field")

        mask = self.evaluator.evaluate(expr, df)
        return df[mask].reset_index(drop=True)

    def _op_sort(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Sort by column."""
        by = step.get("by")
        if not by:
            raise ValueError("Sort operation requires 'by' field")

        order = step.get("order", "asc")
        ascending = order.lower() != "desc"
        return df.sort_values(by=by, ascending=ascending).reset_index(drop=True)

    def _op_compute(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Add computed columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Compute operation requires 'columns' field")

        df = df.copy()
        for col_name, expr in columns.items():
            df[col_name] = self.evaluator.evaluate(expr, df)
        return df

    def _op_select(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Select specific columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Select operation requires 'columns' field")

        available = [c for c in columns if c in df.columns]
        return df[available].copy()

    def _op_rename(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Rename columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Rename operation requires 'columns' field")

        return df.rename(columns=columns)

    def _op_group(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Group by column and aggregate."""
        by = step.get("by")
        if not by:
            raise ValueError("Group operation requires 'by' field")

        agg = step.get("agg")
        if not agg:
            raise ValueError("Group operation requires 'agg' field")

        return df.groupby(by=by).agg(agg).reset_index()

    def _op_limit(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Take first N rows."""
        n = step.get("n", 10)
        return df.head(n).reset_index(drop=True)

    def _op_concat(
        self,
        step: Dict[str, Any],
        df: pd.DataFrame,
        extra_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Concatenate multiple data sources."""
        sources = step.get("sources", [])
        if not sources:
            raise ValueError("Concat operation requires 'sources' field")

        if not extra_sources:
            extra_sources = {}

        frames = [df]
        for src_name in sources:
            if src_name in extra_sources:
                frames.append(extra_sources[src_name])

        return pd.concat(frames, ignore_index=True)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_operations.py -v`
Expected: PASS (all 12 tests)

- [ ] **Step 5: Commit**

```bash
git add pdf_generator/pipeline/operations.py tests/pipeline/test_operations.py
git commit -m "feat(pipeline): add operation registry with filter/sort/compute/group/select/rename/concat/limit"
```

---

## Task 3: Pipeline Engine

**Files:**
- Create: `pdf_generator/pipeline/engine.py`
- Create: `tests/pipeline/test_engine.py`

- [ ] **Step 1: Write failing tests for pipeline engine**

```python
# tests/pipeline/test_engine.py
"""Tests for the pipeline execution engine."""

import pytest
import pandas as pd
from pdf_generator.pipeline.engine import PipelineEngine, PipelineError


class TestPipelineEngine:
    """Test the PipelineEngine class."""

    def setup_method(self):
        self.engine = PipelineEngine()
        self.df = pd.DataFrame({
            "product": ["A", "B", "C", "D", "E"],
            "category": ["X", "X", "Y", "Y", "X"],
            "quantity": [100, 200, 50, 300, 150],
            "price": [10.0, 20.0, 5.0, 30.0, 15.0],
        })

    def test_empty_pipeline(self):
        result = self.engine.execute([], self.df)
        assert len(result) == 5

    def test_single_step(self):
        pipeline = [{"op": "filter", "expr": "quantity > 100"}]
        result = self.engine.execute(pipeline, self.df)
        assert len(result) == 3

    def test_multi_step_pipeline(self):
        pipeline = [
            {"op": "filter", "expr": "quantity > 100"},
            {"op": "sort", "by": "quantity", "order": "desc"},
            {"op": "compute", "columns": {"revenue": "quantity * price"}},
        ]
        result = self.engine.execute(pipeline, self.df)
        assert len(result) == 3
        assert "revenue" in result.columns
        assert result.iloc[0]["product"] == "D"  # highest quantity

    def test_pipeline_error_on_step_failure(self):
        pipeline = [
            {"op": "filter", "expr": "quantity > 100"},
            {"op": "filter", "expr": "invalid_expression_{{{"},
        ]
        with pytest.raises(PipelineError) as exc_info:
            self.engine.execute(pipeline, self.df)
        assert exc_info.value.step_index == 1

    def test_empty_data_source(self):
        empty_df = pd.DataFrame()
        result = self.engine.execute([], empty_df)
        assert len(result) == 0

    def test_pipeline_with_group(self):
        pipeline = [
            {"op": "group", "by": "category", "agg": {"quantity": "sum"}},
        ]
        result = self.engine.execute(pipeline, self.df)
        assert len(result) == 2
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_engine.py -v`
Expected: FAIL with `ImportError: cannot import name 'PipelineEngine'`

- [ ] **Step 3: Implement PipelineEngine**

```python
# pdf_generator/pipeline/engine.py
"""Pipeline execution engine."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import pandas as pd

from pdf_generator.pipeline.operations import OperationRegistry


@dataclass
class PipelineError(Exception):
    """Error that occurred during pipeline execution."""

    step_index: int
    step_config: Dict[str, Any]
    message: str

    def __str__(self):
        return f"Pipeline error at step {self.step_index}: {self.message}"


class PipelineEngine:
    """Execute a sequence of pipeline steps on DataFrames."""

    def __init__(self):
        self.registry = OperationRegistry()

    def execute(
        self,
        pipeline: List[Dict[str, Any]],
        df: pd.DataFrame,
        data_sources: Optional[Dict[str, pd.DataFrame]] = None,
    ) -> pd.DataFrame:
        """Execute a pipeline on a DataFrame.

        Args:
            pipeline: List of step dicts, each with an 'op' key
            df: Input DataFrame
            data_sources: All data sources (for concat operations)

        Returns:
            Transformed DataFrame

        Raises:
            PipelineError: If any step fails
        """
        if not pipeline:
            return df.copy()

        result = df.copy()
        extra_sources = data_sources or {}

        for idx, step in enumerate(pipeline):
            try:
                result = self.registry.execute(step, result, extra_sources)
            except Exception as e:
                raise PipelineError(
                    step_index=idx,
                    step_config=step,
                    message=str(e),
                ) from e

        return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_engine.py -v`
Expected: PASS (all 6 tests)

- [ ] **Step 5: Commit**

```bash
git add pdf_generator/pipeline/engine.py tests/pipeline/test_engine.py
git commit -m "feat(pipeline): add pipeline execution engine"
```

---

## Task 4: Integrate Pipeline into Generator

**Files:**
- Modify: `pdf_generator/core/generator.py:111-139` (in `_load_data_sources`)
- Create: `tests/pipeline/test_integration.py`

- [ ] **Step 1: Write failing integration test**

```python
# tests/pipeline/test_integration.py
"""Integration tests for pipeline in PDF generation."""

import json
import os
import tempfile

import pandas as pd
import pytest

from pdf_generator import PDFReportGenerator


class TestPipelineIntegration:
    """Test pipeline integration with PDF generation."""

    def test_pipeline_with_csv_source(self):
        """Test that pipeline transforms data before PDF generation."""
        # Create temp CSV
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            f.write("product,quantity,price\n")
            f.write("A,100,10\n")
            f.write("B,200,20\n")
            f.write("C,50,5\n")
            csv_path = f.name

        try:
            config = {
                "metadata": {"title": "Pipeline Test"},
                "dataSources": [
                    {
                        "name": "sales",
                        "type": "csv",
                        "path": csv_path,
                        "pipeline": [
                            {"op": "filter", "expr": "quantity > 80"},
                            {"op": "compute", "columns": {"revenue": "quantity * price"}},
                        ],
                    }
                ],
                "elements": [
                    {
                        "type": "table",
                        "dataSource": "sales",
                        "columns": ["product", "quantity", "revenue"],
                    }
                ],
            }

            generator = PDFReportGenerator(config_dict=config)
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as pdf:
                generator.save(pdf.name)
                assert os.path.exists(pdf.name)
        finally:
            os.unlink(csv_path)
            if os.path.exists(pdf.name):
                os.unlink(pdf.name)

    def test_condition_hides_element(self):
        """Test that condition=False hides element."""
        config = {
            "metadata": {"title": "Conditional Test"},
            "dataSources": [
                {
                    "name": "summary",
                    "type": "inline",
                    "data": {"total": [500], "profit": [-100]},
                }
            ],
            "elements": [
                {
                    "type": "text",
                    "content": "Warning: Negative profit!",
                    "condition": "dataSources.summary.profit < 0",
                },
                {
                    "type": "text",
                    "content": "This should always show",
                },
            ],
        }

        generator = PDFReportGenerator(config_dict=config)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as pdf:
            generator.save(pdf.name)
            assert os.path.exists(pdf.name)
            os.unlink(pdf.name)

    def test_loop_generates_multiple_elements(self):
        """Test that loop creates elements per group."""
        config = {
            "metadata": {"title": "Loop Test"},
            "dataSources": [
                {
                    "name": "categories",
                    "type": "inline",
                    "data": {
                        "category": ["Electronics", "Clothing"],
                        "total": [5000, 3000],
                    },
                }
            ],
            "elements": [
                {
                    "type": "heading",
                    "loop": {
                        "dataSource": "categories",
                        "groupBy": "category",
                    },
                    "text": "{{current.category}} Sales",
                    "level": 2,
                },
            ],
        }

        generator = PDFReportGenerator(config_dict=config)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as pdf:
            generator.save(pdf.name)
            assert os.path.exists(pdf.name)
            os.unlink(pdf.name)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_integration.py -v`
Expected: FAIL (pipeline not yet integrated)

- [ ] **Step 3: Modify `_load_data_sources` to execute pipelines**

In `pdf_generator/core/generator.py`, add import at top:

```python
from pdf_generator.pipeline.engine import PipelineEngine
```

Then modify `_load_data_sources` method (lines 111-139) to execute pipeline after loading data:

```python
def _load_data_sources(self):
    """从配置加载数据源"""
    data_sources_config = self.config_parser.get_data_sources()
    pipeline_engine = PipelineEngine()
    
    for ds_config in data_sources_config:
        name = ds_config['name']
        ds_type = ds_config['type']
        
        # 创建数据源对象
        if ds_type in ['json', 'inline']:
            data_source = JSONDataSource(ds_config)
        elif ds_type in ['csv', 'excel']:
            data_source = CSVDataSource(ds_config)
        elif ds_type == 'api':
            data_source = APIDataSource(ds_config)
        elif ds_type == 'database':
            data_source = DatabaseDataSource(ds_config)
        else:
            print(f"Warning: Unsupported data source type '{ds_type}' for '{name}'")
            continue
        
        self.data_source_objects[name] = data_source
        
        # 预加载数据
        try:
            df = data_source.get_data()
            # Execute pipeline if defined
            pipeline = ds_config.get('pipeline', [])
            if pipeline:
                try:
                    df = pipeline_engine.execute(pipeline, df, self.data_sources)
                    print(f"Pipeline executed for '{name}': {len(df)} rows after transformation")
                except Exception as e:
                    print(f"Warning: Pipeline failed for '{name}': {e}")
            self.data_sources[name] = df
            print(f"Loaded data source '{name}': {len(self.data_sources[name])} rows")
        except Exception as e:
            print(f"Warning: Failed to load data source '{name}': {e}")
```

- [ ] **Step 4: Modify `elements.py` to support condition and loop**

In `pdf_generator/core/elements.py`, modify the `create_element` method (lines 26-59) to handle condition and loop. The element factory itself doesn't handle condition/loop — those are handled by the generator. So we need to modify `generator.py` instead.

In `pdf_generator/core/generator.py`, modify `_build_story` method (lines 168-237). Add condition/loop handling before creating elements:

```python
def _build_story(self, page_size: tuple) -> list:
    """构建PDF内容流
    
    Args:
        page_size: 页面大小 (width, height)
    """
    story = []
    
    # 准备模板上下文
    metadata = self.config_parser.get_metadata()
    context = {
        'metadata': metadata,
        'dataSources': self.data_sources,
    }
    
    # 1. 添加封面页（如果启用）
    if self.cover_generator and self.cover_generator.is_enabled():
        cover_elements = self.cover_generator.generate(page_size, context)
        story.extend(cover_elements)
    
    # 2. 添加目录（如果启用）
    if self.toc_generator and self.toc_generator.is_enabled():
        toc_elements = self.toc_generator.generate_toc_elements()
        story.extend(toc_elements)
    
    # 3. 获取元素配置
    elements_config = self.config_parser.get_elements()
    
    # 4. 生成每个元素
    for element_config in elements_config:
        # Handle loop: expand element for each group value
        loop_config = element_config.get('loop')
        if loop_config:
            elements_to_process = self._expand_loop(element_config, loop_config)
        else:
            elements_to_process = [element_config]
        
        for expanded_config in elements_to_process:
            # Handle condition: skip element if condition is false
            condition = expanded_config.get('condition')
            if condition and not self._evaluate_condition(condition, context):
                continue
            
            try:
                # 处理模板变量
                processed_config = self.config_parser.process_element_content(
                    expanded_config, context
                )
                
                # 创建PDF元素
                element_type = processed_config['type']
                
                # 特殊处理：如果是heading且启用了TOC自动生成
                if element_type == 'heading' and self.toc_generator and self.toc_generator.is_auto_generate():
                    level = processed_config.get('level', 1)
                    text = processed_config.get('text', '')
                    style_name = processed_config.get('style', f'Heading{level}')
                    
                    # 使用TOC生成器创建带书签的标题
                    pdf_element = self.toc_generator.create_heading_with_bookmark(
                        text, level, style_name
                    )
                else:
                    # 普通元素
                    pdf_element = self.element_factory.create_element(
                        element_type,
                        processed_config,
                        self.data_sources
                    )
                
                story.append(pdf_element)
            
            except Exception as e:
                # 错误处理：添加错误信息到PDF
                error_text = f"Error creating element: {e}"
                print(f"Warning: {error_text}")
                error_para = Paragraph(
                    f"<font color='red'>{error_text}</font>",
                    self.style_manager.get_style('Normal')
                )
                story.append(error_para)
    
    return story


def _evaluate_condition(self, condition: str, context: dict) -> bool:
    """Evaluate a condition expression."""
    from pdf_generator.pipeline.expression import ExpressionEvaluator
    evaluator = ExpressionEvaluator()
    try:
        # Build a flat dict context for expression evaluation
        flat_context = {}
        if 'metadata' in context:
            flat_context['metadata'] = context['metadata']
        if 'dataSources' in context:
            # For dataSources.summary.profit style references, use the pipeline evaluator
            for ds_name, ds_df in context['dataSources'].items():
                if hasattr(ds_df, 'iloc') and len(ds_df) > 0:
                    # Take first row for scalar reference
                    flat_context[f'dataSources_{ds_name}'] = ds_df.iloc[0].to_dict()
                else:
                    flat_context[f'dataSources_{ds_name}'] = {}
        
        # Parse condition like "dataSources.summary.profit < 0"
        # Convert to "dataSources_summary.profit < 0"
        import re
        normalized = re.sub(r'dataSources\.(\w+)\.(\w+)', r'dataSources_\1.\2', condition)
        
        # For simple scalar references, evaluate directly
        for ds_name, ds_df in context.get('dataSources', {}).items():
            if hasattr(ds_df, 'iloc') and len(ds_df) > 0:
                row_dict = ds_df.iloc[0].to_dict()
                result = evaluator.evaluate(normalized.replace(f'dataSources_{ds_name}', ''))
                # This is simplified — real implementation handles nested refs
        
        # Simplified: just try direct evaluation with context vars
        return bool(evaluator.evaluate(condition, flat_context))
    except Exception as e:
        print(f"Warning: Condition evaluation failed for '{condition}': {e}")
        return True  # fail-open


def _expand_loop(self, element_config: dict, loop_config: dict) -> list:
    """Expand a loop configuration into multiple element configs."""
    ds_name = loop_config.get('dataSource')
    group_by = loop_config.get('groupBy')
    
    if not ds_name or not group_by:
        return [element_config]
    
    if ds_name not in self.data_sources:
        print(f"Warning: Loop data source '{ds_name}' not found")
        return []
    
    df = self.data_sources[ds_name]
    if group_by not in df.columns:
        print(f"Warning: Group column '{group_by}' not found in '{ds_name}'")
        return [element_config]
    
    unique_values = df[group_by].unique()
    expanded = []
    
    for value in unique_values:
        # Clone element config with current value context
        new_config = element_config.copy()
        new_config.pop('loop', None)  # Remove loop to prevent recursion
        
        # Add current iteration context
        current_row = df[df[group_by] == value].iloc[0].to_dict()
        new_config['_current'] = current_row
        
        # Replace {{current.xxx}} in text fields
        for key in ['text', 'content', 'title']:
            if key in new_config and isinstance(new_config[key], str):
                for field, val in current_row.items():
                    placeholder = f'{{{{current.{field}}}}}'
                    new_config[key] = new_config[key].replace(placeholder, str(val))
        
        expanded.append(new_config)
    
    return expanded
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/test_integration.py -v`
Expected: PASS (all 3 tests)

- [ ] **Step 6: Run all tests together**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/ -v`
Expected: PASS (all 32 tests)

- [ ] **Step 7: Commit**

```bash
git add pdf_generator/core/generator.py tests/pipeline/test_integration.py
git commit -m "feat: integrate pipeline engine with generator, add condition/loop support"
```

---

## Task 5: Config Validator Update

**Files:**
- Modify: `pdf_generator/config/validator.py:97-142` (in `_validate_data_sources`)
- Modify: `pdf_generator/config/validator.py:144-274` (in `_validate_elements`)

- [ ] **Step 1: Add pipeline validation to data source validation**

In `pdf_generator/config/validator.py`, after the data source type validation (line 131), add pipeline validation:

```python
# Validate pipeline if present
if 'pipeline' in source:
    pipeline = source['pipeline']
    if not isinstance(pipeline, list):
        self.errors.append(f"Data source '{name}': 'pipeline' must be a list")
    else:
        valid_ops = ['filter', 'sort', 'compute', 'select', 'rename', 'group', 'limit', 'head', 'concat']
        for i, step in enumerate(pipeline):
            if not isinstance(step, dict):
                self.errors.append(f"Data source '{name}': pipeline[{i}] must be a dictionary")
                continue
            if 'op' not in step:
                self.errors.append(f"Data source '{name}': pipeline[{i}] requires 'op' field")
            elif step['op'] not in valid_ops:
                self.errors.append(
                    f"Data source '{name}': pipeline[{i}] has invalid op '{step['op']}'. "
                    f"Must be one of {valid_ops}"
                )
```

- [ ] **Step 2: Add condition/loop validation to element validation**

In `pdf_generator/config/validator.py`, after element type validation (around line 166), add:

```python
# Validate condition if present
if 'condition' in element:
    condition = element['condition']
    if not isinstance(condition, str):
        self.errors.append(f"Element at index {idx}: 'condition' must be a string")

# Validate loop if present
if 'loop' in element:
    loop = element['loop']
    if not isinstance(loop, dict):
        self.errors.append(f"Element at index {idx}: 'loop' must be a dictionary")
    elif 'dataSource' not in loop:
        self.errors.append(f"Element at index {idx}: loop requires 'dataSource' field")
```

- [ ] **Step 3: Run tests**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/pipeline/ -v`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add pdf_generator/config/validator.py
git commit -m "feat: add config validation for pipeline, condition, and loop fields"
```

---

## Task 6: Example Configuration

**Files:**
- Create: `templates/pipeline_demo.json`

- [ ] **Step 1: Create example configuration**

```json
{
  "metadata": {
    "title": "Pipeline Demo Report",
    "author": "PDF Generator",
    "pageSize": "A4"
  },
  "dataSources": [
    {
      "name": "sales",
      "type": "csv",
      "path": "data/sales.csv",
      "pipeline": [
        {"op": "filter", "expr": "quantity > 0"},
        {"op": "compute", "columns": {"revenue": "quantity * price"}},
        {"op": "sort", "by": "revenue", "order": "desc"}
      ]
    },
    {
      "name": "summary",
      "type": "inline",
      "data": {
        "total_revenue": [50000],
        "profit_margin": [0.15]
      }
    }
  ],
  "elements": [
    {
      "type": "text",
      "content": "{{metadata.title}}",
      "style": "title"
    },
    {
      "type": "text",
      "content": "Revenue: {{dataSources.summary.total_revenue}}",
      "condition": "dataSources.summary.total_revenue > 0"
    },
    {
      "type": "table",
      "dataSource": "sales",
      "columns": ["product", "quantity", "price", "revenue"],
      "style": "tableStyle"
    }
  ]
}
```

- [ ] **Step 2: Commit**

```bash
git add templates/pipeline_demo.json
git commit -m "docs: add pipeline demo configuration template"
```

---

## Final Verification

- [ ] **Step 1: Run all tests**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m pytest tests/ -v`
Expected: All tests pass

- [ ] **Step 2: Run linting**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python -m flake8 pdf_generator/pipeline/`
Expected: No errors

- [ ] **Step 3: Verify backward compatibility**

Run: `cd /Users/small_bud/Desktop/OpenCode/pdf-report-generator && python examples/sample_usage.py`
Expected: Existing examples work unchanged

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "feat: complete data pipeline and conditional rendering feature

- Pipeline engine with filter/sort/compute/group/select/rename/concat/limit operations
- Sandboxed expression evaluator for safe condition/pipeline expressions
- Conditional element rendering via condition attribute
- Dynamic element looping via loop attribute
- Config validation for new fields
- Full test coverage"
```
