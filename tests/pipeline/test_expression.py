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
        assert mask.sum() == 2  # rows with (200,20) and (300,30)

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
