"""
22 - Pipeline 数据转换：compute 计算列 + rename 重命名 + select 选择列
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator
from pdf_generator.pipeline import PipelineEngine

raw = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件"],
    "销量": [450, 320, 580, 1200, 890],
    "单价": [5999, 4299, 2999, 3499, 299],
})

engine = PipelineEngine()

# 方式1: compute 计算列
with_calc = engine.execute(
    pipeline=[{"op": "compute", "columns": {"销售额": "销量 * 单价"}}],
    df=raw
)

config1 = {
    "metadata": {"title": "Pipeline - compute"},
    "elements": [
        {"type": "text", "content": "计算列: 销售额 = 销量*单价", "style": "Title"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen1 = PDFReportGenerator(config_dict=config1)
gen1.add_data_source("d", with_calc)
gen1.save("examples/output/22_pipeline_transform_a.pdf")
print("✅ 已生成: examples/output/22_pipeline_transform_a.pdf")

# 方式2: compute + rename + select
transformed = engine.execute(
    pipeline=[
        {"op": "compute", "columns": {"销售额": "销量 * 单价"}},
        {"op": "rename", "columns": {"产品": "产品名称", "销量": "销售数量"}},
        {"op": "select", "columns": ["产品名称", "销售数量", "单价", "销售额"]},
    ],
    df=raw
)

config2 = {
    "metadata": {"title": "Pipeline - rename + select"},
    "elements": [
        {"type": "text", "content": "compute → rename → select", "style": "Title"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen2 = PDFReportGenerator(config_dict=config2)
gen2.add_data_source("d", transformed)
gen2.save("examples/output/22_pipeline_transform_b.pdf")
print("✅ 已生成: examples/output/22_pipeline_transform_b.pdf")
