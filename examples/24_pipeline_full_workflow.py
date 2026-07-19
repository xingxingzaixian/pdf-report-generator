"""
24 - Pipeline 完整工作流：多步骤链式处理 + 生成报告

完整的 ETL 流程：filter → compute → sort → select → rename → 生成PDF
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator
from pdf_generator.pipeline import PipelineEngine

raw = pd.DataFrame({
    "日期": ["2024-01", "2024-01", "2024-02", "2024-02",
             "2024-03", "2024-03", "2024-04", "2024-04"],
    "产品": ["笔记本", "台式机", "笔记本", "台式机",
             "笔记本", "台式机", "笔记本", "台式机"],
    "销量": [120, 80, 145, 90, 160, 95, 180, 100],
    "单价": [5999, 4299, 5899, 4199, 5799, 4099, 5699, 3999],
    "退货": [5, 2, 3, 1, 4, 2, 2, 1],
})

engine = PipelineEngine()

# 完整管道
processed = engine.execute(
    pipeline=[
        {"op": "filter", "expr": "销量 > 50"},
        {"op": "compute", "columns": {
            "销售额": "销量 * 单价",
            "净销量": "销量 - 退货",
            "退货率": "退货 / 销量 * 100"
        }},
        {"op": "sort", "by": "销售额", "order": "desc"},
        {"op": "select", "columns": ["日期", "产品", "销量", "净销量", "单价", "销售额", "退货率"]},
        {"op": "rename", "columns": {"退货率": "退货率(%)"}},
    ],
    df=raw
)

# 按月汇总
monthly = engine.execute(
    pipeline=[{"op": "group", "by": "日期", "agg": {"销售额": "sum", "销量": "sum"}}],
    df=processed
)

config = {
    "metadata": {"title": "Pipeline 完整工作流 - 销售分析"},
    "pageTemplate": {
        "footer": {"enabled": True, "height": 0.5, "center": {"type": "pageNumber", "format": "- {page} -"}}
    },
    "elements": [
        {"type": "text", "content": "销售分析报告（Pipeline处理）", "style": "Title"},
        {"type": "text", "content": "管道步骤: filter → compute → sort → select → rename"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "处理结果明细", "style": "Heading1"},
        {"type": "table", "dataSource": "detail", "style": "Normal"},
        {"type": "pagebreak"},

        {"type": "text", "content": "月度销售额趋势", "style": "Heading1"},
        {
            "type": "chart", "chartType": "line", "dataSource": "monthly",
            "xAxis": "日期", "yAxis": "销售额",
            "title": "月度销售额趋势", "width": 6.5, "height": 4, "grid": True
        },
        {"type": "spacer", "height": 0.3},

        {
            "type": "chart", "chartType": "bar", "dataSource": "monthly",
            "xAxis": "日期", "yAxis": "销量",
            "title": "月度销量对比", "width": 6.5, "height": 3.5, "grid": True
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("detail", processed)
generator.add_data_source("monthly", monthly)
generator.save("examples/output/24_pipeline_full_workflow.pdf")
print("✅ 已生成: examples/output/24_pipeline_full_workflow.pdf")
