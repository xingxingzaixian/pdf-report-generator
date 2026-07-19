"""
04 - CSV 数据源：从 CSV 文件读取数据生成表格

演示 dataSources 配置中 type: csv 的使用方式。
需要 data/sales.csv 文件存在。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "CSV 数据源示例"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC",
            "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF",
            "fontSize": 10,
            "padding": 8
        }
    },
    "dataSources": [
        {"name": "sales_data", "type": "csv", "path": "data/sales.csv"}
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "以下数据从 data/sales.csv 文件中读取："},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales_data", "style": "table"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "数据源配置: {\"name\": \"sales_data\", \"type\": \"csv\", \"path\": \"data/sales.csv\"}", "style": "Normal"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/04_data_csv.pdf")
print("✅ 已生成: examples/output/04_data_csv.pdf")
