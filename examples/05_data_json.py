"""
05 - JSON 数据源：从 JSON 文件读取数据生成图表

演示 dataSources 配置中 type: json 的使用方式。
需要 data/expenses.json 文件存在。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "JSON 数据源示例"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC",
            "headerBackground": "#E67E22",
            "headerTextColor": "#FFFFFF",
            "fontSize": 10,
            "padding": 8
        }
    },
    "dataSources": [
        {"name": "expenses", "type": "json", "path": "data/expenses.json"}
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "数据来源: data/expenses.json"},
        {"type": "spacer", "height": 0.2},

        # 表格展示
        {"type": "text", "content": "支出明细表", "style": "Heading2"},
        {"type": "table", "dataSource": "expenses", "style": "table"},
        {"type": "spacer", "height": 0.3},

        # 图表展示
        {"type": "text", "content": "支出分布图", "style": "Heading2"},
        {
            "type": "chart",
            "dataSource": "expenses",
            "chartType": "bar",
            "xAxis": "类别",
            "yAxis": "金额",
            "title": "各类别支出对比",
            "width": 6.5,
            "height": 4,
            "grid": True
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/05_data_json.pdf")
print("✅ 已生成: examples/output/05_data_json.pdf")
