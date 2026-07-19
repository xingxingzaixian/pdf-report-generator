"""
03 - 简单表格：内嵌数据表格 + 列宽/行高/样式

演示：
1. 直接在配置中嵌入表格数据
2. 自定义列宽和行高
3. 表格样式配置（表头背景色、边框颜色、间距）
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "简单表格示例"},
    "styles": {
        "blueTable": {
            "gridColor": "#BDC3C7", "headerBackground": "#3498DB",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8
        },
        "greenTable": {
            "gridColor": "#95A5A6", "headerBackground": "#27AE60",
            "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 6
        }
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "表格1：自定义列宽（蓝色主题）", "style": "Heading2"},
        {
            "type": "table",
            "data": [
                ["产品", "Q1销量", "Q2销量", "Q3销量", "Q4销量"],
                ["笔记本", "120", "145", "160", "180"],
                ["台式机", "80", "90", "95", "100"],
                ["平板", "200", "220", "250", "280"],
                ["手机", "350", "380", "400", "420"],
            ],
            "style": "blueTable",
            "columnWidths": [2.0, 1.2, 1.2, 1.2, 1.2],
        },
        {"type": "spacer", "height": 0.5},

        {"type": "text", "content": "表格2：自定义行高（绿色主题）", "style": "Heading2"},
        {
            "type": "table",
            "data": [
                ["姓名", "年龄", "部门", "职位"],
                ["张三", "28", "技术部", "高级工程师"],
                ["李四", "32", "销售部", "销售经理"],
                ["王五", "25", "市场部", "市场专员"],
                ["赵六", "35", "技术部", "架构师"],
            ],
            "style": "greenTable",
            "columnWidths": [1.5, 1.0, 1.5, 2.5],
            "rowHeights": [0.4, 0.6, 0.6, 0.6, 0.6],
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/03_simple_table.pdf")
print("✅ 已生成: examples/output/03_simple_table.pdf")
