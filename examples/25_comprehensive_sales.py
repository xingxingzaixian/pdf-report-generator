"""
25 - 综合报告：销售报告（封面+目录+图表+表格+页眉页脚）

使用 config dataSources inline 内联数据，无需 add_data_source。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

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
    "dataSources": [
        {
            "name": "sales",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "Q1": 120, "Q2": 145, "Q3": 160, "Q4": 180, "单价": 5999, "年销量": 605, "年销售额": 3629395},
                {"产品": "台式机", "Q1": 80, "Q2": 90, "Q3": 95, "Q4": 100, "单价": 4299, "年销量": 365, "年销售额": 1569135},
                {"产品": "平板", "Q1": 200, "Q2": 220, "Q3": 250, "Q4": 280, "单价": 2999, "年销量": 950, "年销售额": 2849050},
                {"产品": "手机", "Q1": 350, "Q2": 380, "Q3": 400, "Q4": 420, "单价": 3499, "年销量": 1550, "年销售额": 5418250},
                {"产品": "配件", "Q1": 500, "Q2": 520, "Q3": 550, "Q4": 580, "单价": 299, "年销量": 2150, "年销售额": 642850},
            ]
        }
    ],
    "elements": [
        {"type": "heading", "text": "一、销售总览", "level": 1},
        {"type": "text", "content": "2024年度各产品线销售数据汇总（数据通过 config dataSources inline 加载）："},
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
        {"type": "text", "content": "3.1 各产品年销售额"},
        {
            "type": "chart", "chartType": "bar", "dataSource": "sales",
            "xAxis": "产品", "yAxis": "年销售额",
            "title": "各产品年销售额（元）", "width": 6.5, "height": 3.5, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "四、结论与建议", "level": 1},
        {"type": "text", "content": "1. 手机和配件产品线销量领先，贡献了最大的市场份额。"},
        {"type": "text", "content": "2. 笔记本虽然销量不及移动产品，但因单价高，销售额可观。"},
        {"type": "text", "content": "3. 建议下一年度加大对移动产品线的投入。"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "报告生成日期：{{date}}"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/25_comprehensive_sales.pdf")
print("✅ 已生成: examples/output/25_comprehensive_sales.pdf")
