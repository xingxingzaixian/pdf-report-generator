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
