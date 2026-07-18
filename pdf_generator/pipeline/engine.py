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
