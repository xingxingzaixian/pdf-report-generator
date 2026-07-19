"""
20 - 表格样式变体：斑马纹、边框样式、配色方案

演示多种表格视觉风格：
- 斑马纹（alternateRowColor）
- 不同表头配色方案
- 深色/浅色主题
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

data = [
    ["产品", "Q1", "Q2", "Q3", "Q4"],
    ["笔记本", "120", "145", "160", "180"],
    ["台式机", "80", "90", "95", "100"],
    ["平板", "200", "220", "250", "280"],
    ["手机", "350", "380", "400", "420"],
]

config = {
    "metadata": {"title": "表格样式变体"},
    "styles": {
        "blueZebra": {
            "gridColor": "#D5D8DC", "headerBackground": "#2980B9",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 7,
            "alternateRowColor": "#EBF5FB"
        },
        "darkTheme": {
            "gridColor": "#34495E", "headerBackground": "#2C3E50",
            "headerTextColor": "#ECF0F1", "fontSize": 9, "padding": 7,
            "alternateRowColor": "#3D566E", "textColor": "#ECF0F1"
        },
        "minimal": {
            "gridColor": "#E5E7E9", "headerBackground": "#F8F9F9",
            "headerTextColor": "#2C3E50", "fontSize": 9, "padding": 7,
        },
        "greenTheme": {
            "gridColor": "#A9DFBF", "headerBackground": "#1E8449",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 7,
            "alternateRowColor": "#EAFAF1"
        },
        "warmTheme": {
            "gridColor": "#F5B7B1", "headerBackground": "#C0392B",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 7,
            "alternateRowColor": "#FDEDEC"
        },
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "1. 经典蓝 + 斑马纹", "style": "Heading2"},
        {"type": "table", "data": data, "style": "blueZebra", "columnWidths": [2,1,1,1,1]},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "2. 深色主题", "style": "Heading2"},
        {"type": "table", "data": data, "style": "darkTheme", "columnWidths": [2,1,1,1,1]},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "3. 简约风格", "style": "Heading2"},
        {"type": "table", "data": data, "style": "minimal", "columnWidths": [2,1,1,1,1]},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "4. 绿色主题", "style": "Heading2"},
        {"type": "table", "data": data, "style": "greenTheme", "columnWidths": [2,1,1,1,1]},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "5. 暖色主题", "style": "Heading2"},
        {"type": "table", "data": data, "style": "warmTheme", "columnWidths": [2,1,1,1,1]},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/20_table_style_variants.pdf")
print("✅ 已生成: examples/output/20_table_style_variants.pdf")
