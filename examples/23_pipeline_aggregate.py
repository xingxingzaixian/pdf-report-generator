"""
23 - Pipeline 分组聚合与合并：group + concat

演示两种使用方式：
1. config dataSources 中直接配置 pipeline（推荐）
2. 独立 PipelineEngine API
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: config 中内嵌 pipeline — group 分组聚合
# ============================================================
config1 = {
    "metadata": {"title": "Pipeline 内嵌 - group 分组聚合"},
    "dataSources": [
        {
            "name": "raw",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "区域": "华北", "销量": 120, "金额": 719880},
                {"产品": "台式机", "区域": "华北", "销量": 80, "金额": 343920},
                {"产品": "平板", "区域": "华北", "销量": 200, "金额": 599800},
                {"产品": "手机", "区域": "华东", "销量": 350, "金额": 1224650},
                {"产品": "配件", "区域": "华东", "销量": 500, "金额": 149500},
                {"产品": "笔记本", "区域": "华东", "销量": 100, "金额": 599900},
                {"产品": "台式机", "区域": "华东", "销量": 70, "金额": 300930},
                {"产品": "平板", "区域": "华东", "销量": 180, "金额": 539820},
            ]
        },
        {
            "name": "agg",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "区域": "华北", "销量": 120, "金额": 719880},
                {"产品": "台式机", "区域": "华北", "销量": 80, "金额": 343920},
                {"产品": "平板", "区域": "华北", "销量": 200, "金额": 599800},
                {"产品": "手机", "区域": "华东", "销量": 350, "金额": 1224650},
                {"产品": "配件", "区域": "华东", "销量": 500, "金额": 149500},
                {"产品": "笔记本", "区域": "华东", "销量": 100, "金额": 599900},
                {"产品": "台式机", "区域": "华东", "销量": 70, "金额": 300930},
                {"产品": "平板", "区域": "华东", "销量": 180, "金额": 539820},
            ],
            "pipeline": [
                {"op": "group", "by": "区域", "agg": {"销量": "sum", "金额": "sum"}},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "按区域汇总销量和金额", "style": "Title"},
        {"type": "text", "content": "原始数据 8 条 → group by 区域 → 2 条汇总"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "原始数据:", "style": "Heading2"},
        {"type": "table", "dataSource": "raw", "style": "Normal"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "聚合结果:", "style": "Heading2"},
        {"type": "table", "dataSource": "agg", "style": "Normal"},
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)
gen1.save("examples/output/23_pipeline_aggregate_a.pdf")
print("✅ 已生成: examples/output/23_pipeline_aggregate_a.pdf")


# ============================================================
# 方式2: 独立 PipelineEngine — concat 合并多数据源
# ============================================================
from pdf_generator.pipeline import PipelineEngine
import pandas as pd

engine = PipelineEngine()
north = pd.DataFrame({"产品": ["笔记本", "台式机"], "区域": ["华北", "华北"], "销量": [120, 80]})
south = pd.DataFrame({"产品": ["平板", "手机"], "区域": ["华南", "华南"], "销量": [200, 350]})
east = pd.DataFrame({"产品": ["配件", "显示器"], "区域": ["华东", "华东"], "销量": [500, 300]})

merged = engine.execute(
    pipeline=[{"op": "concat", "sources": ["north", "south", "east"]}],
    df=north,
    data_sources={"north": north, "south": south, "east": east}
)

config2 = {
    "metadata": {"title": "Pipeline API - concat 合并"},
    "elements": [
        {"type": "text", "content": "三区域数据合并（PipelineEngine API）", "style": "Title"},
        {"type": "text", "content": "concat: 华北 + 华南 + 华东 → 一个表"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen2 = PDFReportGenerator(config_dict=config2)
gen2.add_data_source("d", merged)
gen2.save("examples/output/23_pipeline_aggregate_b.pdf")
print("✅ 已生成: examples/output/23_pipeline_aggregate_b.pdf")
