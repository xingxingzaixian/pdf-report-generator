"""
23 - Pipeline 分组聚合与合并：group 分组聚合 + concat 合并数据源
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator
from pdf_generator.pipeline import PipelineEngine

engine = PipelineEngine()

# 方式1: group 分组聚合
sales = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件", "笔记本", "台式机", "平板"],
    "区域": ["华北", "华北", "华北", "华东", "华东", "华东", "华东", "华东"],
    "销量": [120, 80, 200, 350, 500, 100, 70, 180],
    "金额": [719880, 343920, 599800, 1224650, 149500, 599900, 300930, 539820],
})

agg = engine.execute(
    pipeline=[{"op": "group", "by": "区域", "agg": {"销量": "sum", "金额": "sum"}}],
    df=sales
)

config1 = {
    "metadata": {"title": "Pipeline - 分组聚合"},
    "elements": [
        {"type": "text", "content": "按区域汇总销量和金额", "style": "Title"},
        {"type": "text", "content": "原始数据8条 → 按区域分组 → 2条汇总"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "原始数据:", "style": "Heading2"},
        {"type": "table", "dataSource": "raw", "style": "Normal"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "聚合结果:", "style": "Heading2"},
        {"type": "table", "dataSource": "agg", "style": "Normal"},
    ]
}
gen1 = PDFReportGenerator(config_dict=config1)
gen1.add_data_source("raw", sales)
gen1.add_data_source("agg", agg)
gen1.save("examples/output/23_pipeline_aggregate_a.pdf")
print("✅ 已生成: examples/output/23_pipeline_aggregate_a.pdf")

# 方式2: concat 合并
north = pd.DataFrame({"产品": ["笔记本", "台式机"], "区域": ["华北", "华北"], "销量": [120, 80]})
south = pd.DataFrame({"产品": ["平板", "手机"], "区域": ["华南", "华南"], "销量": [200, 350]})
east = pd.DataFrame({"产品": ["配件", "显示器"], "区域": ["华东", "华东"], "销量": [500, 300]})

merged = engine.execute(
    pipeline=[{"op": "concat", "sources": ["north", "south", "east"]}],
    df=north,
    data_sources={"north": north, "south": south, "east": east}
)

config2 = {
    "metadata": {"title": "Pipeline - 合并数据源"},
    "elements": [
        {"type": "text", "content": "三区域数据合并", "style": "Title"},
        {"type": "text", "content": "concat: 华北+华南+华东 → 一个表"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen2 = PDFReportGenerator(config_dict=config2)
gen2.add_data_source("d", merged)
gen2.save("examples/output/23_pipeline_aggregate_b.pdf")
print("✅ 已生成: examples/output/23_pipeline_aggregate_b.pdf")
