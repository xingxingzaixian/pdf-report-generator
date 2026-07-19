"""
24 - Pipeline 完整工作流：多步骤链式处理 + 生成报告

演示两种使用方式：
1. config dataSources 中内嵌完整 pipeline（推荐）
2. 独立 PipelineEngine API + add_data_source
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: config 中内嵌完整 pipeline（推荐 — 无需 Python 管道代码）
# ============================================================
config1 = {
    "metadata": {"title": "Pipeline 内嵌 - 完整工作流"},
    "pageTemplate": {
        "footer": {"enabled": True, "height": 0.5,
                   "center": {"type": "pageNumber", "format": "- {page} -"}}
    },
    "dataSources": [
        {
            "name": "raw",
            "type": "inline",
            "data": [
                {"日期": "2024-01", "产品": "笔记本", "销量": 120, "单价": 5999, "退货": 5},
                {"日期": "2024-01", "产品": "台式机", "销量": 80, "单价": 4299, "退货": 2},
                {"日期": "2024-02", "产品": "笔记本", "销量": 145, "单价": 5899, "退货": 3},
                {"日期": "2024-02", "产品": "台式机", "销量": 90, "单价": 4199, "退货": 1},
                {"日期": "2024-03", "产品": "笔记本", "销量": 160, "单价": 5799, "退货": 4},
                {"日期": "2024-03", "产品": "台式机", "销量": 95, "单价": 4099, "退货": 2},
                {"日期": "2024-04", "产品": "笔记本", "销量": 180, "单价": 5699, "退货": 2},
                {"日期": "2024-04", "产品": "台式机", "销量": 100, "单价": 3999, "退货": 1},
            ]
        },
        {
            "name": "processed",
            "type": "inline",
            "data": [
                {"日期": "2024-01", "产品": "笔记本", "销量": 120, "单价": 5999, "退货": 5},
                {"日期": "2024-01", "产品": "台式机", "销量": 80, "单价": 4299, "退货": 2},
                {"日期": "2024-02", "产品": "笔记本", "销量": 145, "单价": 5899, "退货": 3},
                {"日期": "2024-02", "产品": "台式机", "销量": 90, "单价": 4199, "退货": 1},
                {"日期": "2024-03", "产品": "笔记本", "销量": 160, "单价": 5799, "退货": 4},
                {"日期": "2024-03", "产品": "台式机", "销量": 95, "单价": 4099, "退货": 2},
                {"日期": "2024-04", "产品": "笔记本", "销量": 180, "单价": 5699, "退货": 2},
                {"日期": "2024-04", "产品": "台式机", "销量": 100, "单价": 3999, "退货": 1},
            ],
            "pipeline": [
                {"op": "filter", "expr": "销量 > 50"},
                {"op": "compute", "columns": {
                    "销售额": "销量 * 单价",
                    "净销量": "销量 - 退货",
                    "退货率": "退货 / 销量 * 100"
                }},
                {"op": "sort", "by": "销售额", "order": "desc"},
                {"op": "select", "columns": ["日期", "产品", "销量", "净销量", "单价", "销售额", "退货率"]},
                {"op": "rename", "columns": {"退货率": "退货率(%)"}},
            ]
        },
        {
            "name": "monthly",
            "type": "inline",
            "data": [
                {"日期": "2024-01", "产品": "笔记本", "销量": 120, "单价": 5999, "退货": 5},
                {"日期": "2024-01", "产品": "台式机", "销量": 80, "单价": 4299, "退货": 2},
                {"日期": "2024-02", "产品": "笔记本", "销量": 145, "单价": 5899, "退货": 3},
                {"日期": "2024-02", "产品": "台式机", "销量": 90, "单价": 4199, "退货": 1},
                {"日期": "2024-03", "产品": "笔记本", "销量": 160, "单价": 5799, "退货": 4},
                {"日期": "2024-03", "产品": "台式机", "销量": 95, "单价": 4099, "退货": 2},
                {"日期": "2024-04", "产品": "笔记本", "销量": 180, "单价": 5699, "退货": 2},
                {"日期": "2024-04", "产品": "台式机", "销量": 100, "单价": 3999, "退货": 1},
            ],
            "pipeline": [
                {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
                {"op": "group", "by": "日期", "agg": {"销售额": "sum", "销量": "sum"}},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "销售分析报告（Pipeline 内嵌处理）", "style": "Title"},
        {"type": "text", "content": "所有数据处理都在 config dataSources 的 pipeline 中完成"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "处理结果明细", "style": "Heading1"},
        {"type": "table", "dataSource": "processed", "style": "Normal"},
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

gen1 = PDFReportGenerator(config_dict=config1)
gen1.save("examples/output/24_pipeline_full_workflow_a.pdf")
print("✅ 已生成: examples/output/24_pipeline_full_workflow_a.pdf")


# ============================================================
# 方式2: 独立 PipelineEngine API + add_data_source
# ============================================================
# from pdf_generator.pipeline import PipelineEngine
# import pandas as pd
#
# engine = PipelineEngine()
# raw = pd.DataFrame({...})
# processed = engine.execute(
#     pipeline=[
#         {"op": "filter", "expr": "销量 > 50"},
#         {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
#         {"op": "sort", "by": "销售额", "order": "desc"},
#     ],
#     df=raw
# )
# generator = PDFReportGenerator(config_dict=config)
# generator.add_data_source("processed", processed)
# generator.save("output.pdf")
