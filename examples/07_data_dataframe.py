"""
07 - 编程注入数据源：DataFrame / dict / list 多种数据类型

演示 add_data_source() 支持的所有数据类型：
1. pandas DataFrame
2. dict（自动转换为 DataFrame）
3. list of dict（自动转换为 DataFrame）

同时展示 config dataSources 中 inline 方式的等效写法。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator


# ============================================================
# 方式1: 注入 pandas DataFrame
# ============================================================
sales_df = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件"],
    "Q1": [120, 80, 200, 350, 500],
    "Q2": [145, 90, 220, 380, 520],
})

config1 = {
    "metadata": {"title": "DataFrame 注入"},
    "elements": [
        {"type": "text", "content": "pandas DataFrame 数据", "style": "Title"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "Normal"},
    ]
}
gen1 = PDFReportGenerator(config_dict=config1)
gen1.add_data_source("sales", sales_df)
gen1.save("examples/output/07_data_dataframe_a.pdf")
print("✅ 已生成: examples/output/07_data_dataframe_a.pdf")


# ============================================================
# 方式2: 注入 dict — add_data_source 自动转为 DataFrame
# ============================================================
sales_dict = {
    "产品": ["笔记本", "台式机", "平板"],
    "销量": [450, 320, 580],
    "单价": [5999, 4299, 2999],
}

config2 = {
    "metadata": {"title": "dict 数据注入"},
    "elements": [
        {"type": "text", "content": "dict 自动转为 DataFrame", "style": "Title"},
        {"type": "text", "content": "add_data_source 支持 dict 类型，自动转换。"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "Normal"},
    ]
}
gen2 = PDFReportGenerator(config_dict=config2)
gen2.add_data_source("sales", sales_dict)
gen2.save("examples/output/07_data_dataframe_b.pdf")
print("✅ 已生成: examples/output/07_data_dataframe_b.pdf")


# ============================================================
# 方式3: 注入 list of dict — 自动转为 DataFrame
# ============================================================
sales_list = [
    {"产品": "笔记本", "销量": 450, "单价": 5999},
    {"产品": "台式机", "销量": 320, "单价": 4299},
    {"产品": "平板", "销量": 580, "单价": 2999},
]

config3 = {
    "metadata": {"title": "list of dict 数据注入"},
    "elements": [
        {"type": "text", "content": "list of dict 自动转为 DataFrame", "style": "Title"},
        {"type": "text", "content": "add_data_source 也支持 list of dict。"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "sales", "style": "Normal"},
    ]
}
gen3 = PDFReportGenerator(config_dict=config3)
gen3.add_data_source("sales", sales_list)
gen3.save("examples/output/07_data_dataframe_c.pdf")
print("✅ 已生成: examples/output/07_data_dataframe_c.pdf")


# ============================================================
# 等效方式: config dataSources inline（无需 add_data_source）
# ============================================================
# config = {
#     "dataSources": [{
#         "name": "sales",
#         "type": "inline",
#         "data": [
#             {"产品": "笔记本", "销量": 450, "单价": 5999},
#             {"产品": "台式机", "销量": 320, "单价": 4299},
#         ]
#     }],
#     "elements": [{"type": "table", "dataSource": "sales"}]
# }
