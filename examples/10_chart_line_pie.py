"""
10 - 折线图与饼图

演示 chart 元素的折线图和饼图配置方式。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator

# 折线图数据
trend_data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "收入": [100000, 120000, 115000, 130000, 140000, 155000],
    "支出": [80000, 85000, 90000, 88000, 92000, 95000],
    "利润": [20000, 35000, 25000, 42000, 48000, 60000],
})

# 饼图数据
pie_data = pd.DataFrame({
    "类别": ["人力成本", "运营成本", "营销费用", "研发投入", "其他"],
    "金额": [450000, 200000, 150000, 300000, 100000],
})

config = {
    "metadata": {"title": "折线图与饼图示例"},
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        # 折线图 - 单线
        {"type": "text", "content": "1. 折线图 - 收入趋势", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "line",
            "dataSource": "trend",
            "xAxis": "月份",
            "yAxis": "收入",
            "title": "月度收入趋势",
            "width": 6.5,
            "height": 3.5,
            "grid": True
        },
        {"type": "pagebreak"},

        # 折线图 - 多线
        {"type": "text", "content": "2. 折线图 - 多指标对比", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "line",
            "dataSource": "trend",
            "xAxis": "月份",
            "yAxis": ["收入", "支出", "利润"],
            "title": "月度经营趋势",
            "width": 6.5,
            "height": 4,
            "grid": True
        },
        {"type": "pagebreak"},

        # 饼图
        {"type": "text", "content": "3. 饼图 - 成本构成", "style": "Heading2"},
        {
            "type": "chart",
            "chartType": "pie",
            "dataSource": "cost",
            "xAxis": "类别",
            "yAxis": "金额",
            "title": "年度成本构成",
            "width": 6,
            "height": 4.5,
            "grid": False
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("trend", trend_data)
generator.add_data_source("cost", pie_data)
generator.save("examples/output/10_chart_line_pie.pdf")
print("✅ 已生成: examples/output/10_chart_line_pie.pdf")
