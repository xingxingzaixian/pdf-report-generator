"""
19 - 表格布局：跨页重复表头、间距、对齐、自动换行

演示表格的高级布局参数：
- repeatRows: 跨页时每页重复表头
- hAlign: 表格在页面中的水平对齐
- spaceBefore/spaceAfter: 表格前后间距
- wrapColumns/wrapThreshold: 自动换行
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

data = [["ID", "产品名称", "类别", "价格", "库存"]]
for i in range(1, 41):
    data.append([
        str(i),
        f"超长产品名称-第{i}号商品",
        "电子" if i % 3 == 0 else "家居" if i % 3 == 1 else "服装",
        f"¥{100 + i * 10}",
        str(50 + i * 5)
    ])

config = {
    "metadata": {"title": "表格布局示例"},
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "text", "content": "本表格应用了多个布局参数：跨页重复表头、居中、自动换行"},
        {"type": "spacer", "height": 0.2},
        {
            "type": "table",
            "data": data,
            "columnWidths": [0.6, 2.5, 1.2, 1.2, 1.0],
            "repeatRows": 1,
            "hAlign": "CENTER",
            "vAlign": "TOP",
            "spaceBefore": 0.3,
            "spaceAfter": 0.3,
            "wrapColumns": [1],
            "wrapThreshold": 15
        },
        {"type": "text", "content": "表格布局参数说明:", "style": "Heading2"},
        {"type": "text", "content": "• repeatRows: 1 — 跨页时每页显示表头"},
        {"type": "text", "content": "• hAlign: CENTER — 表格在页面居中"},
        {"type": "text", "content": "• spaceBefore/After: 0.3 — 前后间距"},
        {"type": "text", "content": "• wrapColumns: [1] — 产品名称列自动换行"},
        {"type": "text", "content": "• wrapThreshold: 15 — 超过15字符换行"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/19_table_layout.pdf")
print("✅ 已生成: examples/output/19_table_layout.pdf")
