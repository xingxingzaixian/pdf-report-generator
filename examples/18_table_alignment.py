"""
18 - 单元格对齐：全局样式对齐 vs cellAlignments 精确控制

演示两种对齐方式：
1. 通过样式设置全局对齐（所有单元格统一）
2. 通过 cellAlignments 精确控制每个单元格
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "单元格对齐示例"},
    "styles": {
        "leftTop": {
            "gridColor": "#CCCCCC", "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 8,
            "alignment": "LEFT", "valignment": "TOP"
        },
        "centerMiddle": {
            "gridColor": "#CCCCCC", "headerBackground": "#70AD47",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 8,
            "alignment": "CENTER", "valignment": "MIDDLE"
        },
        "rightBottom": {
            "gridColor": "#CCCCCC", "headerBackground": "#FFC000",
            "headerTextColor": "#000000", "fontSize": 9, "padding": 8,
            "alignment": "RIGHT", "valignment": "BOTTOM"
        }
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "一、通过样式设置全局对齐", "style": "Heading1"},

        {"type": "text", "content": "左对齐 + 顶部对齐", "style": "Heading2"},
        {"type": "table", "data": [["姓名","年龄","部门"],["张三","28","技术部"],["李四","32","销售部"]],
         "style": "leftTop", "columnWidths": [2,1.5,2], "rowHeights": [0.4,0.6,0.6]},

        {"type": "text", "content": "居中对齐 + 中间对齐", "style": "Heading2"},
        {"type": "table", "data": [["产品","价格","库存"],["产品A","¥1,200","50"],["产品B","¥800","120"]],
         "style": "centerMiddle", "columnWidths": [2,1.5,2], "rowHeights": [0.4,0.6,0.6]},

        {"type": "text", "content": "右对齐 + 底部对齐", "style": "Heading2"},
        {"type": "table", "data": [["项目","金额","状态"],["项目X","$5,000","进行中"],["项目Y","$8,000","已完成"]],
         "style": "rightBottom", "columnWidths": [2,1.5,2], "rowHeights": [0.4,0.6,0.6]},
        {"type": "pagebreak"},

        {"type": "text", "content": "二、cellAlignments 精确控制", "style": "Heading1"},
        {"type": "text", "content": "财务报告：名称左对齐，金额右对齐，状态居中"},
        {"type": "spacer", "height": 0.2},
        {
            "type": "table",
            "data": [
                ["项目名称", "Q1", "Q2", "Q3", "Q4", "总计", "状态"],
                ["营业收入", "50,000", "55,000", "60,000", "65,000", "230,000", "良好"],
                ["营业成本", "30,000", "32,000", "35,000", "38,000", "135,000", "正常"],
                ["毛利润", "20,000", "23,000", "25,000", "27,000", "95,000", "优秀"],
            ],
            "columnWidths": [1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8],
            "rowHeights": [0.4, 0.5, 0.5, 0.5],
            "cellAlignments": [
                {"range": [0, 0, 3, 0], "align": "LEFT", "valign": "MIDDLE"},
                {"range": [0, 1, 3, 5], "align": "RIGHT", "valign": "MIDDLE"},
                {"range": [0, 6, 3, 6], "align": "CENTER", "valign": "MIDDLE"},
            ],
            "hAlign": "CENTER",
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/18_table_alignment.pdf")
print("✅ 已生成: examples/output/18_table_alignment.pdf")
