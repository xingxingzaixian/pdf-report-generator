"""
12 - 页眉页脚：三栏布局、文本/图片/日期变量

演示 pageTemplate 中 header 和 footer 的配置：
- 左中右三栏布局
- 文本、页码、图片元素
- 模板变量 {{metadata.xxx}} 和 {{date}}
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "页眉页脚演示",
        "author": "PDF Generator",
        "company": "示例科技有限公司"
    },
    "pageTemplate": {
        "header": {
            "enabled": True,
            "height": 0.8,
            "showLine": True,
            "left": {"type": "text", "content": "{{metadata.title}}", "fontSize": 9},
            "center": {"type": "text", "content": "内部文档", "fontSize": 9},
            "right": {"type": "text", "content": "{{date}}", "fontSize": 9}
        },
        "footer": {
            "enabled": True,
            "height": 0.6,
            "showLine": True,
            "left": {"type": "text", "content": "{{metadata.company}}", "fontSize": 8},
            "center": {
                "type": "pageNumber",
                "format": "第{page}页 / 共{total}页",
                "fontSize": 8
            },
            "right": {"type": "text", "content": "保密", "fontSize": 8, "color": "#FF0000"}
        }
    },
    "elements": [
        {"type": "text", "content": "页眉页脚功能演示", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "观察每一页的顶部和底部：", "style": "Normal"},
        {"type": "text", "content": "页眉 - 左: 文档标题 | 中: \"内部文档\" | 右: 日期", "style": "Normal"},
        {"type": "text", "content": "页脚 - 左: 公司名称 | 中: 页码 | 右: \"保密\"(红色)", "style": "Normal"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第二页 - 页码会自动更新", "style": "Heading1"},
        {"type": "text", "content": "翻到这一页，查看页脚的页码是否变为 '第2页 / 共3页'。"},
        {"type": "pagebreak"},
        {"type": "text", "content": "第三页 - 最后一页", "style": "Heading1"},
        {"type": "text", "content": "所有页面的页眉页脚保持一致，仅页码变化。"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/12_header_footer.pdf")
print("✅ 已生成: examples/output/12_header_footer.pdf")
