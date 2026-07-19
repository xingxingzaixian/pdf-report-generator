"""
25 - 综合报告：销售报告（封面+目录+图表+表格+页眉页脚）

演示将多个功能组合成一份完整的专业销售报告。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator

sales = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件"],
    "Q1": [120, 80, 200, 350, 500],
    "Q2": [145, 90, 220, 380, 520],
    "Q3": [160, 95, 250, 400, 550],
    "Q4": [180, 100, 280, 420, 580],
    "单价": [5999, 4299, 2999, 3499, 299],
    "年销量": [605, 365, 950, 1550, 2150],
    "年销售额": [3629395, 1569135, 2849050, 5418250, 642850],
})

config = {
    "metadata": {
        "title": "2024年度销售分析报告",
        "author": "销售部",
        "company": "示例科技有限公司"
    },
    "coverPage": {
        "enabled": True,
        "background": {"type": "gradient", "colorStart": "#1a1a2e", "colorEnd": "#16213e"},
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "Title",
             "position": {"x": "center", "y": 500}},
            {"type": "text", "content": "{{metadata.company}}", "style": "Heading1",
             "position": {"x": "center", "y": 400}},
            {"type": "text", "content": "编制：{{metadata.author}} | {{date}}", "style": "Normal",
             "position": {"x": "center", "y": 200}},
        ]
    },
    "toc": {"enabled": True, "autoGenerate": True, "title": "目  录", "maxLevel": 2},
    "pageTemplate": {
        "header": {
            "enabled": True, "height": 0.7, "showLine": True,
            "left": {"type": "text", "content": "{{metadata.title}}", "fontSize": 8},
            "right": {"type": "text", "content": "{{date}}", "fontSize": 8}
        },
        "footer": {
            "enabled": True, "height": 0.5, "showLine": True,
            "center": {"type": "pageNumber", "format": "- {page} -", "fontSize": 8}
        }
    },
    "styles": {
        "salesTable": {
            "gridColor": "#BDC3C7", "headerBackground": "#2980B9",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 7,
            "alternateRowColor": "#EBF5FB"
        }
    },
    "elements": [
        {"type": "heading", "text": "一、销售总览", "level": 1},
        {"type": "text", "content": "2024年度各产品线销售数据汇总如下："},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "salesTable",
         "columnWidths": [1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2]},
        {"type": "pagebreak"},

        {"type": "heading", "text": "二、季度趋势分析", "level": 1},
        {"type": "text", "content": "2.1 各产品季度销量对比"},
        {
            "type": "chart", "chartType": "bar", "dataSource": "sales",
            "xAxis": "产品", "yAxis": ["Q1", "Q2", "Q3", "Q4"],
            "title": "季度销量对比", "width": 6.5, "height": 4, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "三、销售额分析", "level": 1},
        {"type": "text", "content": "3.1 各产品年销售额占比"},
        {
            "type": "chart", "chartType": "pie", "dataSource": "sales",
            "xAxis": "产品", "yAxis": "年销售额",
            "title": "年销售额占比", "width": 6, "height": 4.5
        },
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "3.2 产品销量与销售额对比"},
        {
            "type": "chart", "chartType": "bar", "dataSource": "sales",
            "xAxis": "产品", "yAxis": "年销售额",
            "title": "各产品年销售额（元）", "width": 6.5, "height": 3.5, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "四、结论与建议", "level": 1},
        {"type": "text", "content": "根据以上数据分析："},
        {"type": "text", "content": "1. 手机和配件产品线销量领先，贡献了最大的市场份额。"},
        {"type": "text", "content": "2. 笔记本虽然销量不及移动产品，但因单价高，销售额可观。"},
        {"type": "text", "content": "3. 建议下一年度加大对移动产品线的投入，同时优化台式机产品定位。"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "报告生成日期：{{date}}", "style": "Normal"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", sales)
generator.save("examples/output/25_comprehensive_sales.pdf")
print("✅ 已生成: examples/output/25_comprehensive_sales.pdf")
