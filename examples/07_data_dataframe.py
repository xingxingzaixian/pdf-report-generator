"""
07 - DataFrame 数据源：编程方式注入 pandas DataFrame

演示通过 add_data_source() 方法动态注入数据，
无需依赖外部文件，适合从数据库或其他来源获取数据后动态生成报告。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator

# 方式1: 从字典创建 DataFrame
sales = pd.DataFrame({
    "产品": ["笔记本", "台式机", "平板", "手机", "配件"],
    "Q1": [120, 80, 200, 350, 500],
    "Q2": [145, 90, 220, 380, 520],
    "Q3": [160, 95, 250, 400, 550],
    "Q4": [180, 100, 280, 420, 580],
})

# 方式2: 从列表创建 DataFrame（带中文列名）
employees = pd.DataFrame([
    {"姓名": "张三", "部门": "技术部", "工龄": 5, "绩效": "A"},
    {"姓名": "李四", "部门": "销售部", "工龄": 3, "绩效": "B"},
    {"姓名": "王五", "部门": "技术部", "工龄": 7, "绩效": "A"},
    {"姓名": "赵六", "部门": "市场部", "工龄": 2, "绩效": "C"},
    {"姓名": "钱七", "部门": "销售部", "工龄": 4, "绩效": "B"},
])

config = {
    "metadata": {"title": "DataFrame 动态数据源"},
    "styles": {
        "blueTable": {
            "gridColor": "#BDC3C7",
            "headerBackground": "#2980B9",
            "headerTextColor": "#FFFFFF",
            "fontSize": 10,
            "padding": 8
        },
        "greenTable": {
            "gridColor": "#BDC3C7",
            "headerBackground": "#27AE60",
            "headerTextColor": "#FFFFFF",
            "fontSize": 10,
            "padding": 8
        }
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        # 数据源1: sales
        {"type": "text", "content": "销售数据（蓝色主题）", "style": "Heading2"},
        {"type": "table", "dataSource": "sales", "style": "blueTable"},
        {"type": "spacer", "height": 0.3},

        # 图表
        {"type": "text", "content": "季度销量趋势", "style": "Heading2"},
        {
            "type": "chart",
            "dataSource": "sales",
            "chartType": "line",
            "xAxis": "产品",
            "yAxis": ["Q1", "Q2", "Q3", "Q4"],
            "title": "各产品季度销量趋势",
            "width": 6.5,
            "height": 4,
            "grid": True
        },
        {"type": "pagebreak"},

        # 数据源2: employees
        {"type": "text", "content": "员工信息（绿色主题）", "style": "Heading2"},
        {"type": "table", "dataSource": "employees", "style": "greenTable"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", sales)
generator.add_data_source("employees", employees)
generator.save("examples/output/07_data_dataframe.pdf")
print("✅ 已生成: examples/output/07_data_dataframe.pdf")
