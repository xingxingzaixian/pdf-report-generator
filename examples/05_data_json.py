"""
05 - JSON 数据源 + inline 内联数据

演示 dataSources 的两种 JSON 配置方式：
1. type: json — 从 JSON 文件加载
2. type: inline — 数据直接写在 config 中（无需外部文件）
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: JSON 文件数据源
# ============================================================
config1 = {
    "metadata": {"title": "JSON 文件数据源"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC", "headerBackground": "#E67E22",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8
        }
    },
    "dataSources": [
        {"name": "expenses", "type": "json", "path": "data/expenses.json"}
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "text", "content": "数据来源: data/expenses.json"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "expenses", "style": "table"},
        {"type": "spacer", "height": 0.3},
        {
            "type": "chart", "dataSource": "expenses",
            "chartType": "bar", "xAxis": "类别", "yAxis": "金额",
            "title": "各类别支出对比", "width": 6.5, "height": 4, "grid": True
        },
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)
gen1.save("examples/output/05_data_json_a.pdf")
print("✅ 已生成: examples/output/05_data_json_a.pdf")


# ============================================================
# 方式2: inline 内联数据 — 数据直接写在 config 中
# ============================================================
config2 = {
    "metadata": {"title": "Inline 内联数据源"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC", "headerBackground": "#8E44AD",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8
        }
    },
    "dataSources": [
        {
            "name": "products",
            "type": "inline",
            "data": [
                {"产品": "笔记本", "Q1": 120, "Q2": 145, "Q3": 160, "Q4": 180},
                {"产品": "台式机", "Q1": 80, "Q2": 90, "Q3": 95, "Q4": 100},
                {"产品": "平板", "Q1": 200, "Q2": 220, "Q3": 250, "Q4": 280},
                {"产品": "手机", "Q1": 350, "Q2": 380, "Q3": 400, "Q4": 420},
            ]
        }
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "text", "content": "数据直接写在 config 的 dataSources 中，无需外部文件。"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "products", "style": "table"},
    ]
}

gen2 = PDFReportGenerator(config_dict=config2)
gen2.save("examples/output/05_data_json_b.pdf")
print("✅ 已生成: examples/output/05_data_json_b.pdf")
