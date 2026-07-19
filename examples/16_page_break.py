"""
16 - 分页控制：pagebreak 元素 + 页面方向切换

演示：
1. pagebreak 元素手动分页
2. metadata.orientation 控制页面方向（portrait/landscape）
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "分页与页面方向演示",
        "orientation": "portrait"
    },
    "elements": [
        {"type": "text", "content": "分页控制演示", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "当前页面: 第1页（竖屏 portrait）", "style": "Heading2"},
        {"type": "text", "content": "使用 pagebreak 元素可以手动控制分页。"},
        {"type": "text", "content": "以下是一段填充文本，用来展示竖屏模式下的布局效果。"},
        {"type": "text", "content": "竖屏模式（portrait）适合大多数文档，如报告、手册等。"},

        {"type": "pagebreak"},

        {"type": "text", "content": "当前页面: 第2页（竖屏 portrait）", "style": "Heading2"},
        {"type": "text", "content": "这是通过 pagebreak 分出来的第二页。"},
        {"type": "text", "content": "注意：同一份 PDF 目前使用统一的页面方向。"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "pagebreak 的常见使用场景:", "style": "Heading2"},
        {"type": "text", "content": "1. 每个章节从新页开始"},
        {"type": "text", "content": "2. 图表独占一页"},
        {"type": "text", "content": "3. 封面/目录后的正文分页"},
        {"type": "text", "content": "4. 附录单独分页"},

        {"type": "pagebreak"},

        {"type": "text", "content": "当前页面: 第3页", "style": "Heading2"},
        {"type": "text", "content": "横向布局（landscape）适合宽表格、大图表等场景。"},
        {"type": "text", "content": "在 metadata 中设置 \"orientation\": \"landscape\" 即可切换。"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "orientation 选项:", "style": "Heading2"},
        {"type": "text", "content": "• portrait - 竖屏（默认），适合文字内容"},
        {"type": "text", "content": "• landscape - 横屏，适合宽表格和图表"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/16_page_break.pdf")
print("✅ 已生成: examples/output/16_page_break.pdf")
