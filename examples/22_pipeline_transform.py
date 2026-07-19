"""
22 - Pipeline 数据转换：compute + rename + select

演示两种使用方式：
1. config dataSources 中直接配置 pipeline
2. 独立 PipelineEngine API
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: config 中内嵌 pipeline — compute 计算列
# ============================================================
config1 = {
    "metadata": {"title": "Pipeline 内嵌 - compute"},
    "dataSources": [
        {
            "name": "calc",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "销量": 450, "单价": 5999},
                {"产品": "台式机", "销量": 320, "单价": 4299},
                {"产品": "平板", "销量": 580, "单价": 2999},
                {"产品": "手机", "销量": 1200, "单价": 3499},
                {"产品": "配件", "销量": 890, "单价": 299},
            ],
            "pipeline": [
                {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "compute: 销售额 = 销量 × 单价", "style": "Title"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "calc", "style": "Normal"},
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)
gen1.save("examples/output/22_pipeline_transform_a.pdf")
print("✅ 已生成: examples/output/22_pipeline_transform_a.pdf")


# ============================================================
# 方式2: config 中内嵌 pipeline — compute + rename + select 链式处理
# ============================================================
config2 = {
    "metadata": {"title": "Pipeline - 链式处理"},
    "dataSources": [
        {
            "name": "transformed",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "销量": 450, "单价": 5999, "备注": "热销"},
                {"产品": "台式机", "销量": 320, "单价": 4299, "备注": "一般"},
                {"产品": "平板", "销量": 580, "单价": 2999, "备注": "热销"},
                {"产品": "手机", "销量": 1200, "单价": 3499, "备注": "爆款"},
                {"产品": "配件", "销量": 890, "单价": 299, "备注": "热销"},
            ],
            "pipeline": [
                {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
                {"op": "rename", "columns": {"产品": "产品名称", "销量": "销售数量"}},
                {"op": "select", "columns": ["产品名称", "销售数量", "单价", "销售额"]},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "compute → rename → select", "style": "Title"},
        {"type": "text", "content": "管道: 计算销售额 → 重命名列 → 选择列"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "transformed", "style": "Normal"},
    ]
}

gen2 = PDFReportGenerator(config_dict=config2)
gen2.save("examples/output/22_pipeline_transform_b.pdf")
print("✅ 已生成: examples/output/22_pipeline_transform_b.pdf")


# ============================================================
# 等效方式: 独立 PipelineEngine API
# ============================================================
# from pdf_generator.pipeline import PipelineEngine
# import pandas as pd
#
# engine = PipelineEngine()
# raw = pd.DataFrame({...})
# result = engine.execute(
#     pipeline=[
#         {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
#         {"op": "rename", "columns": {"产品": "产品名称"}},
#         {"op": "select", "columns": ["产品名称", "销售额"]},
#     ],
#     df=raw
# )
