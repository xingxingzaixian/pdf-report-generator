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
        """Execute a single pipeline step."""
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

    def _op_filter(self, step, df, extra_sources):
        """Filter rows by expression."""
        expr = step.get("expr")
        if not expr:
            raise ValueError("Filter operation requires 'expr' field")
        mask = self.evaluator.evaluate(expr, df)
        return df[mask].reset_index(drop=True)

    def _op_sort(self, step, df, extra_sources):
        """Sort by column."""
        by = step.get("by")
        if not by:
            raise ValueError("Sort operation requires 'by' field")
        order = step.get("order", "asc")
        ascending = order.lower() != "desc"
        return df.sort_values(by=by, ascending=ascending).reset_index(drop=True)

    def _op_compute(self, step, df, extra_sources):
        """Add computed columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Compute operation requires 'columns' field")
        df = df.copy()
        for col_name, expr in columns.items():
            df[col_name] = self.evaluator.evaluate(expr, df)
        return df

    def _op_select(self, step, df, extra_sources):
        """Select specific columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Select operation requires 'columns' field")
        available = [c for c in columns if c in df.columns]
        return df[available].copy()

    def _op_rename(self, step, df, extra_sources):
        """Rename columns."""
        columns = step.get("columns")
        if not columns:
            raise ValueError("Rename operation requires 'columns' field")
        return df.rename(columns=columns)

    def _op_group(self, step, df, extra_sources):
        """Group by column and aggregate."""
        by = step.get("by")
        if not by:
            raise ValueError("Group operation requires 'by' field")
        agg = step.get("agg")
        if not agg:
            raise ValueError("Group operation requires 'agg' field")
        return df.groupby(by=by).agg(agg).reset_index()

    def _op_limit(self, step, df, extra_sources):
        """Take first N rows."""
        n = step.get("n", 10)
        return df.head(n).reset_index(drop=True)

    def _op_concat(self, step, df, extra_sources):
        """Concatenate multiple data sources."""
        sources = step.get("sources", [])
        if not sources:
            raise ValueError("Concat operation requires 'sources' field")
        if not extra_sources:
            extra_sources = {}
        frames = []
        for src_name in sources:
            if src_name in extra_sources:
                frames.append(extra_sources[src_name])
        return pd.concat(frames, ignore_index=True)
