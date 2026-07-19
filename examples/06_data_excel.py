"""
06 - Excel 数据源：通过 config 的 dataSources 配置加载 Excel

演示 dataSources 中 type: excel 的使用方式。
支持 .xlsx 和 .xls 格式，可指定 sheet 名称。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "Excel 数据源"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC", "headerBackground": "#8E44AD",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8,
            "alternateRowColor": "#F5EEF8"
        }
    },
    "dataSources": [
        {
            "name": "sales",
            "type": "excel",
            "path": "data/sales.xlsx"
            # "sheetName": "Sheet1"   # 可选：指定 sheet 名称
        }
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "数据来源: data/sales.xlsx（紫色主题 + 斑马纹）"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "table"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/06_data_excel.pdf")
print("✅ 已生成: examples/output/06_data_excel.pdf")
