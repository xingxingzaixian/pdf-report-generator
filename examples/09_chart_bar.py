"""
09 - 柱状图：单Y轴、多Y轴、堆叠柱状图

演示 chart 元素的多种柱状图配置方式。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator

data = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件"],
    "Q1": [120, 80, 200, 350, 500],
    "Q2": [145, 90, 220, 380, 520],
    "Q3": [160, 95, 250, 400, 550],
    "Q4": [180, 100, 280, 420, 580],
    "销售额": [2699550, 1375680, 1739420, 4198800, 266110],
})

config = {
    "metadata": {"title": "柱状图示例"},
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        # 单Y轴柱状图
        {"type": "text", "content": "1. 单Y轴柱状图 - 产品销量对比", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "Q4",
            "title": "Q4各产品销量对比",
            "width": 6.5,
            "height": 3.5,
            "grid": True
        },
        {"type": "pagebreak"},

        # 多Y轴柱状图
        {"type": "text", "content": "2. 多Y轴柱状图 - 季度对比", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": ["Q1", "Q2", "Q3", "Q4"],
            "title": "各产品四季度销量对比",
            "width": 6.5,
            "height": 4,
            "grid": True
        },
        {"type": "pagebreak"},

        # 水平柱状图
        {"type": "text", "content": "3. 水平柱状图 - 销售额", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销售额",
            "title": "各产品销售额（元）",
            "width": 6.5,
            "height": 3.5,
            "grid": True
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)
generator.save("examples/output/09_chart_bar.pdf")
print("✅ 已生成: examples/output/09_chart_bar.pdf")
