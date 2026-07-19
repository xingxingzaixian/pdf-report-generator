"""
21 - Pipeline 过滤与排序：filter + sort + limit

演示使用 PipelineEngine 对数据进行预处理。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator
from pdf_generator.pipeline import PipelineEngine

raw = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件", "显示器", "键盘", "鼠标"],
    "Q1": [120, 80, 200, 350, 500, 300, 600, 800],
    "Q2": [145, 90, 220, 380, 520, 320, 620, 820],
    "价格": [5999, 4299, 2999, 3499, 299, 1999, 199, 99],
})

engine = PipelineEngine()

# 方式1: filter + sort
filtered = engine.execute(
    pipeline=[
        {"op": "filter", "expr": "Q1 > 200"},
        {"op": "sort", "by": "Q1", "order": "desc"},
    ],
    df=raw
)

config1 = {
    "metadata": {"title": "Pipeline - 过滤与排序"},
    "elements": [
        {"type": "text", "content": "过滤与排序结果", "style": "Title"},
        {"type": "text", "content": "管道: filter Q1>200 → sort Q1 desc"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen1 = PDFReportGenerator(config_dict=config1)
gen1.add_data_source("d", filtered)
gen1.save("examples/output/21_pipeline_filter_a.pdf")
print("✅ 已生成: examples/output/21_pipeline_filter_a.pdf")

# 方式2: limit Top N
top3 = engine.execute(
    pipeline=[{"op": "sort", "by": "Q2", "order": "desc"}, {"op": "limit", "n": 3}],
    df=raw
)

config2 = {
    "metadata": {"title": "Pipeline - Top 3"},
    "elements": [
        {"type": "text", "content": "Q2销量 Top 3", "style": "Title"},
        {"type": "text", "content": "管道: sort Q2 desc → limit n=3"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "d", "style": "Normal"},
    ]
}
gen2 = PDFReportGenerator(config_dict=config2)
gen2.add_data_source("d", top3)
gen2.save("examples/output/21_pipeline_filter_b.pdf")
print("✅ 已生成: examples/output/21_pipeline_filter_b.pdf")
