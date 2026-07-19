"""
26 - 综合报告：财务报告（合并表格+多图表+管道预处理）

演示一个完整的财务报告，使用 Pipeline 预处理数据，
结合合并表格和多图表展示。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator
from pdf_generator.pipeline import PipelineEngine

# 原始财务数据
raw = pd.DataFrame({
    "月份": ["1月", "1月", "2月", "2月", "3月", "3月", "4月", "4月", "5月", "5月", "6月", "6月"],
    "类别": ["收入", "支出", "收入", "支出", "收入", "支出", "收入", "支出", "收入", "支出", "收入", "支出"],
    "金额": [100000, 80000, 120000, 85000, 115000, 90000, 130000, 88000, 140000, 92000, 155000, 95000],
})

engine = PipelineEngine()

# 管道处理：分离收入/支出并计算利润
income = engine.execute(
    pipeline=[
        {"op": "filter", "expr": "类别 == '收入'"},
        {"op": "select", "columns": ["月份", "金额"]},
        {"op": "rename", "columns": {"金额": "收入"}},
    ],
    df=raw
)

expense = engine.execute(
    pipeline=[
        {"op": "filter", "expr": "类别 == '支出'"},
        {"op": "select", "columns": ["月份", "金额"]},
        {"op": "rename", "columns": {"金额": "支出"}},
    ],
    df=raw
)

# 合并并计算利润
income["支出"] = expense["支出"].values
income["利润"] = income["收入"] - income["支出"]
income["利润率"] = (income["利润"] / income["收入"] * 100).round(1)

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
    "elements": [
        {"type": "heading", "text": "一、财务总览", "level": 1},
        {"type": "text", "content": "以下为2024年上半年各月财务数据汇总（Pipeline 处理后）："},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "finance", "style": "financeTable",
         "columnWidths": [1.2, 1.5, 1.5, 1.5, 1.2]},
        {"type": "pagebreak"},

        {"type": "heading", "text": "二、趋势分析", "level": 1},
        {"type": "text", "content": "2.1 收入与支出趋势"},
        {
            "type": "chart", "chartType": "line", "dataSource": "finance",
            "xAxis": "月份", "yAxis": ["收入", "支出", "利润"],
            "title": "月度经营趋势", "width": 6.5, "height": 4, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "text", "content": "2.2 利润率走势"},
        {
            "type": "chart", "chartType": "line", "dataSource": "finance",
            "xAxis": "月份", "yAxis": "利润率",
            "title": "月度利润率（%）", "width": 6.5, "height": 3.5, "grid": True
        },
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "2.3 收入结构"},
        {
            "type": "chart", "chartType": "bar", "dataSource": "finance",
            "xAxis": "月份", "yAxis": ["收入", "利润"],
            "title": "收入与利润对比", "width": 6.5, "height": 3.5, "grid": True
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "三、总结", "level": 1},
        {"type": "text", "content": "上半年财务表现总结："},
        {"type": "text", "content": f"• 总收入: ¥{income['收入'].sum():,}"},
        {"type": "text", "content": f"• 总支出: ¥{income['支出'].sum():,}"},
        {"type": "text", "content": f"• 总利润: ¥{income['利润'].sum():,}"},
        {"type": "text", "content": f"• 平均利润率: {income['利润率'].mean():.1f}%"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "整体经营状况良好，利润率稳定在较高水平。建议继续控制成本，提升盈利能力。"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("finance", income)
generator.save("examples/output/26_comprehensive_financial.pdf")
print("✅ 已生成: examples/output/26_comprehensive_financial.pdf")
