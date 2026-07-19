"""
26 - 综合报告：财务报告（合并表格+多图表+pipeline 预处理）

使用 config dataSources + pipeline 内嵌处理，无需 add_data_source。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "2024上半年财务分析报告",
        "author": "财务部",
        "company": "示例科技有限公司"
    },
    "coverPage": {
        "enabled": True,
        "background": {"type": "color", "color": "#FFFFFF"},
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "Title",
             "position": {"x": "center", "y": 550}},
            {"type": "text", "content": "{{metadata.company}}", "style": "Heading1",
             "position": {"x": "center", "y": 450}},
            {"type": "text", "content": "编制部门：{{metadata.author}}", "style": "Normal",
             "position": {"x": "center", "y": 220}},
            {"type": "text", "content": "{{date}}", "style": "Normal",
             "position": {"x": "center", "y": 180}},
        ]
    },
    "toc": {"enabled": True, "autoGenerate": True, "title": "目  录", "maxLevel": 2},
    "pageTemplate": {
        "header": {
            "enabled": True, "height": 0.7, "showLine": True,
            "left": {"type": "text", "content": "{{metadata.title}}"},
            "right": {"type": "text", "content": "{{date}}"}
        },
        "footer": {
            "enabled": True, "height": 0.5, "showLine": True,
            "left": {"type": "text", "content": "保密", "color": "#FF0000", "fontSize": 8},
            "center": {"type": "pageNumber", "format": "第{page}页 / 共{total}页"},
            "right": {"type": "text", "content": "{{metadata.company}}", "fontSize": 8}
        }
    },
    "styles": {
        "financeTable": {
            "gridColor": "#CCCCCC", "headerBackground": "#1F4788",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8
        }
    },
    "dataSources": [
        {
            "name": "raw",
            "type": "inline",
            "data": [
                {"月份": "1月", "类别": "收入", "金额": 100000},
                {"月份": "1月", "类别": "支出", "金额": 80000},
                {"月份": "2月", "类别": "收入", "金额": 120000},
                {"月份": "2月", "类别": "支出", "金额": 85000},
                {"月份": "3月", "类别": "收入", "金额": 115000},
                {"月份": "3月", "类别": "支出", "金额": 90000},
                {"月份": "4月", "类别": "收入", "金额": 130000},
                {"月份": "4月", "类别": "支出", "金额": 88000},
                {"月份": "5月", "类别": "收入", "金额": 140000},
                {"月份": "5月", "类别": "支出", "金额": 92000},
                {"月份": "6月", "类别": "收入", "金额": 155000},
                {"月份": "6月", "类别": "支出", "金额": 95000},
            ]
        },
        {
            "name": "income",
            "type": "inline",
            "data": [
                {"月份": "1月", "类别": "收入", "金额": 100000},
                {"月份": "1月", "类别": "支出", "金额": 80000},
                {"月份": "2月", "类别": "收入", "金额": 120000},
                {"月份": "2月", "类别": "支出", "金额": 85000},
                {"月份": "3月", "类别": "收入", "金额": 115000},
                {"月份": "3月", "类别": "支出", "金额": 90000},
                {"月份": "4月", "类别": "收入", "金额": 130000},
                {"月份": "4月", "类别": "支出", "金额": 88000},
                {"月份": "5月", "类别": "收入", "金额": 140000},
                {"月份": "5月", "类别": "支出", "金额": 92000},
                {"月份": "6月", "类别": "收入", "金额": 155000},
                {"月份": "6月", "类别": "支出", "金额": 95000},
            ],
            "pipeline": [
                {"op": "filter", "expr": "类别 == '收入'"},
                {"op": "select", "columns": ["月份", "金额"]},
                {"op": "rename", "columns": {"金额": "收入"}},
            ]
        },
        {
            "name": "expense",
            "type": "inline",
            "data": [
                {"月份": "1月", "类别": "收入", "金额": 100000},
                {"月份": "1月", "类别": "支出", "金额": 80000},
                {"月份": "2月", "类别": "收入", "金额": 120000},
                {"月份": "2月", "类别": "支出", "金额": 85000},
                {"月份": "3月", "类别": "收入", "金额": 115000},
                {"月份": "3月", "类别": "支出", "金额": 90000},
                {"月份": "4月", "类别": "收入", "金额": 130000},
                {"月份": "4月", "类别": "支出", "金额": 88000},
                {"月份": "5月", "类别": "收入", "金额": 140000},
                {"月份": "5月", "类别": "支出", "金额": 92000},
                {"月份": "6月", "类别": "收入", "金额": 155000},
                {"月份": "6月", "类别": "支出", "金额": 95000},
            ],
            "pipeline": [
                {"op": "filter", "expr": "类别 == '支出'"},
                {"op": "select", "columns": ["月份", "金额"]},
                {"op": "rename", "columns": {"金额": "支出"}},
            ]
        }
    ],
    "elements": [
        {"type": "heading", "text": "一、财务总览", "level": 1},
        {"type": "text", "content": "原始数据通过 pipeline 自动分离为收入和支出两个数据源。"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "收入明细:", "style": "Heading2"},
        {"type": "table", "dataSource": "income", "style": "financeTable", "columnWidths": [2, 3]},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "支出明细:", "style": "Heading2"},
        {"type": "table", "dataSource": "expense", "style": "financeTable", "columnWidths": [2, 3]},
        {"type": "pagebreak"},

        {"type": "heading", "text": "二、趋势分析", "level": 1},
        {"type": "text", "content": "2.1 收入趋势"},
        {
            "type": "chart", "chartType": "line", "dataSource": "income",
            "xAxis": "月份", "yAxis": "收入",
            "title": "月度收入趋势", "width": 6.5, "height": 4, "grid": True
        },
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "2.2 支出趋势"},
        {
            "type": "chart", "chartType": "bar", "dataSource": "expense",
            "xAxis": "月份", "yAxis": "支出",
            "title": "月度支出对比", "width": 6.5, "height": 3.5, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "三、总结", "level": 1},
        {"type": "text", "content": "所有数据处理均通过 config dataSources 中的 pipeline 完成。"},
        {"type": "text", "content": "数据源配置示例:"},
        {"type": "text", "content": '{"name": "income", "type": "inline", "data": [...], "pipeline": [{"op": "filter", ...}]}'},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/26_comprehensive_financial.pdf")
print("✅ 已生成: examples/output/26_comprehensive_financial.pdf")
