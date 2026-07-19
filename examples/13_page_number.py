"""
13 - 页码格式：阿拉伯数字、罗马数字、中文数字

演示 pageNumber 元素支持的所有页码格式。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "页码格式演示"},
    "pageTemplate": {
        "footer": {
            "enabled": True,
            "height": 0.8,
            "left": {
                "type": "pageNumber",
                "format": "阿拉伯: {page}"
            },
            "center": {
                "type": "pageNumber",
                "format": "罗马: {page:roman}"
            },
            "right": {
                "type": "pageNumber",
                "format": "中文: 第{page:chinese}页"
            }
        }
    },
    "elements": [
        {"type": "text", "content": "页码格式演示", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "查看每页页脚的三种页码格式："},
        {"type": "text", "content": "• 左侧: 阿拉伯数字 ({page})"},
        {"type": "text", "content": "• 中间: 罗马数字 ({page:roman})"},
        {"type": "text", "content": "• 右侧: 中文数字 ({page:chinese})"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "支持的格式:", "style": "Heading2"},
        {"type": "text", "content": "{page} 或 {page:arabic} - 阿拉伯数字: 1, 2, 3..."},
        {"type": "text", "content": "{page:roman} - 大写罗马数字: I, II, III..."},
        {"type": "text", "content": "{page:roman_lower} - 小写罗马数字: i, ii, iii..."},
        {"type": "text", "content": "{page:chinese} - 中文数字: 一, 二, 三..."},
        {"type": "text", "content": "{page}/{total} - 第1/5页格式"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第二页", "style": "Heading1"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第三页", "style": "Heading1"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第四页", "style": "Heading1"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第五页", "style": "Heading1"},
        {"type": "text", "content": "注意观察页脚中三种页码格式的差异。"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/13_page_number.pdf")
print("✅ 已生成: examples/output/13_page_number.pdf")
