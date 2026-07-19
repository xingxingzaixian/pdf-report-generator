"""
04 - CSV 数据源：通过 config 的 dataSources 配置加载 CSV

演示 dataSources 中 type: csv 的使用方式。
数据源在 config 中配置，生成器自动加载，无需 add_data_source。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: config 中配置 CSV 数据源（推荐）
# ============================================================
config = {
    "metadata": {"title": "CSV 数据源 - config 配置"},
    "styles": {
        "table": {
            "gridColor": "#CCCCCC", "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8
        }
    },
    "dataSources": [
        {"name": "sales", "type": "csv", "path": "data/sales.csv"}
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "数据来源: data/sales.csv（通过 dataSources 配置自动加载）"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "table"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/04_data_csv.pdf")
print("✅ 已生成: examples/output/04_data_csv.pdf")


# ============================================================
# 方式2: 编程方式注入（也支持，作为备选说明）
# ============================================================
# import pandas as pd
# df = pd.read_csv("data/sales.csv")
# generator = PDFReportGenerator(config_dict=config_no_ds)
# generator.add_data_source("sales", df)
# generator.save("output.pdf")
