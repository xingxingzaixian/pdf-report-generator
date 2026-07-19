"""
21 - Pipeline 过滤与排序：filter + sort + limit

演示两种使用方式：
1. config dataSources 中直接配置 pipeline（推荐）
2. 独立 PipelineEngine API 编程调用

Pipeline 操作的数据都是 pd.DataFrame，因为系统内部统一使用 DataFrame。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: config 中内嵌 pipeline（推荐 — 无需额外代码）
# ============================================================
config1 = {
    "metadata": {"title": "Pipeline 内嵌 - filter + sort"},
    "dataSources": [
        {
            "name": "filtered",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "Q1": 120, "Q2": 145, "价格": 5999},
                {"产品": "台式机", "Q1": 80, "Q2": 90, "价格": 4299},
                {"产品": "平板", "Q1": 200, "Q2": 220, "价格": 2999},
                {"产品": "手机", "Q1": 350, "Q2": 380, "价格": 3499},
                {"产品": "配件", "Q1": 500, "Q2": 520, "价格": 299},
            ],
            "pipeline": [
                {"op": "filter", "expr": "Q1 > 150"},         # 只保留 Q1 > 150
                {"op": "sort", "by": "Q1", "order": "desc"},   # 按 Q1 降序
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "filter + sort 结果", "style": "Title"},
        {"type": "text", "content": "管道步骤（在 config 中配置）:"},
        {"type": "text", "content": '1. filter: Q1 > 150'},
        {"type": "text", "content": '2. sort: by=Q1, order=desc'},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "filtered", "style": "Normal"},
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)
gen1.save("examples/output/21_pipeline_filter_a.pdf")
print("✅ 已生成: examples/output/21_pipeline_filter_a.pdf")


# ============================================================
# 方式2: 独立 PipelineEngine API 编程调用
# ============================================================
# from pdf_generator.pipeline import PipelineEngine
# import pandas as pd
#
# engine = PipelineEngine()
# raw = pd.DataFrame({...})
# result = engine.execute(
#     pipeline=[
#         {"op": "filter", "expr": "Q1 > 150"},
#         {"op": "sort", "by": "Q1", "order": "desc"},
#     ],
#     df=raw  # 传入 DataFrame
# )
# generator.add_data_source("filtered", result)

# ============================================================
# 方式3: limit 取 Top N（在 config 中内嵌 pipeline）
# ============================================================
config2 = {
    "metadata": {"title": "Pipeline - Top 3"},
    "dataSources": [
        {
            "name": "top3",
            "type": "inline",
            "data": [
                {"产品": "鼠标", "Q2": 820},
                {"产品": "键盘", "Q2": 620},
                {"产品": "配件", "Q2": 520},
                {"产品": "手机", "Q2": 380},
                {"产品": "显示器", "Q2": 320},
                {"产品": "平板", "Q2": 220},
            ],
            "pipeline": [
                {"op": "sort", "by": "Q2", "order": "desc"},
                {"op": "limit", "n": 3},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "Q2销量 Top 3", "style": "Title"},
        {"type": "text", "content": "管道: sort Q2 desc → limit n=3"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "top3", "style": "Normal"},
    ]
}

gen2 = PDFReportGenerator(config_dict=config2)
gen2.save("examples/output/21_pipeline_filter_b.pdf")
print("✅ 已生成: examples/output/21_pipeline_filter_b.pdf")
