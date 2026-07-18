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
