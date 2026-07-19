"""
02 - 文本与样式：文本元素 + 预设/自定义样式

演示：
1. 使用系统预设样式（Title, Heading1, Heading2, Normal）
2. 自定义样式（字体大小、颜色、加粗、对齐、间距）
3. 模板变量 {{metadata.xxx}}
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "文本与样式演示",
        "author": "PDF Generator",
        "date": "2024年12月"
    },
    "styles": {
        "customTitle": {
            "fontSize": 24, "textColor": "#2C3E50",
            "alignment": "center", "bold": True, "spaceAfter": 20
        },
        "customSubtitle": {
            "fontSize": 14, "textColor": "#7F8C8D",
            "alignment": "center", "spaceAfter": 30
        },
        "highlight": {
            "fontSize": 12, "textColor": "#E74C3C",
            "bold": True, "spaceBefore": 10, "spaceAfter": 5
        },
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "customTitle"},
        {"type": "text", "content": "作者: {{metadata.author}} | 日期: {{metadata.date}}", "style": "customSubtitle"},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "一、使用预设样式", "style": "Heading1"},
        {"type": "text", "content": "系统提供了 Title、Heading1、Heading2、Heading3、Normal 等预设样式。", "style": "Normal"},

        {"type": "text", "content": "1.1 Heading2 样式", "style": "Heading2"},
        {"type": "text", "content": "这是一段 Normal 样式的正文文本。", "style": "Normal"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "二、自定义样式", "style": "Heading1"},
        {"type": "text", "content": "⚠ 重要提示", "style": "highlight"},
        {"type": "text", "content": "自定义样式可以完全控制字体大小、颜色、粗细、对齐和间距。", "style": "Normal"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/02_text_styles.pdf")
print("✅ 已生成: examples/output/02_text_styles.pdf")
