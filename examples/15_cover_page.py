"""
15 - 封面页：纯色/渐变背景、文本自由定位

演示 coverPage 配置的两种背景类型：
- 渐变背景（gradient）
- 纯色背景（color）
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "2024年度分析报告",
        "author": "数据分析部",
        "company": "示例科技有限公司"
    },
    "coverPage": {
        "enabled": True,
        "background": {
            "type": "gradient",
            "colorStart": "#1a1a2e",
            "colorEnd": "#16213e"
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "Title",
                "position": {"x": "center", "y": 500}
            },
            {
                "type": "text",
                "content": "{{metadata.company}}",
                "style": "Heading1",
                "position": {"x": "center", "y": 400}
            },
            {
                "type": "text",
                "content": "编制：{{metadata.author}}",
                "style": "Normal",
                "position": {"x": "center", "y": 200}
            },
            {
                "type": "text",
                "content": "{{date}}",
                "style": "Normal",
                "position": {"x": "center", "y": 150}
            }
        ]
    },
    "elements": [
        {"type": "heading", "text": "第一章 概述", "level": 1},
        {"type": "text", "content": "这个 PDF 演示了封面页功能。封面使用了深色渐变背景。"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "封面元素包括:"},
        {"type": "text", "content": "• 报告标题 - 位置 y=500"},
        {"type": "text", "content": "• 公司名称 - 位置 y=400"},
        {"type": "text", "content": "• 编制人 - 位置 y=200"},
        {"type": "text", "content": "• 日期 - 位置 y=150"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "封面背景支持两种类型:", "style": "Heading2"},
        {"type": "text", "content": "1. gradient - 渐变色（colorStart + colorEnd）"},
        {"type": "text", "content": "2. color - 纯色背景"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/15_cover_page.pdf")
print("✅ 已生成: examples/output/15_cover_page.pdf")
