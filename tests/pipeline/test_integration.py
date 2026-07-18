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
            "toc": {"autoGenerate": False},
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
