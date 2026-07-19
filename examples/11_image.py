"""
11 - 图片插入：对齐方式、保持比例、指定尺寸

演示 image 元素的各种配置方式：
- 左对齐 / 居中 / 右对齐
- 保持宽高比 vs 固定尺寸
- 不同尺寸的图片
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# 确保 demo.png 存在
demo_path = os.path.join(os.path.dirname(__file__), "demo.png")
if not os.path.exists(demo_path):
    print("⚠️  demo.png 不存在，正在生成...")
    try:
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (400, 200), color='#3498DB')
        draw = ImageDraw.Draw(img)
        draw.rectangle([10, 10, 390, 190], outline='white', width=3)
        draw.text((200, 80), "PDF Generator", fill='white', anchor="mm")
        draw.text((200, 120), "Demo Image", fill='white', anchor="mm")
        img.save(demo_path)
        print("✅ demo.png 已生成")
    except Exception as e:
        print(f"❌ 无法创建 demo.png: {e}")
        sys.exit(1)

config = {
    "metadata": {"title": "图片插入示例"},
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        # 居中对齐 + 保持比例
        {"type": "text", "content": "1. 居中对齐（保持宽高比）", "style": "Heading2"},
        {"type": "text", "content": "width=400, height=200, keepAspectRatio=True, alignment=center"},
        {
            "type": "image",
            "path": "examples/demo.png",
            "width": 400,
            "height": 200,
            "alignment": "center",
            "keepAspectRatio": True
        },
        {"type": "spacer", "height": 0.5},

        # 左对齐 + 固定尺寸
        {"type": "text", "content": "2. 左对齐（固定尺寸，不保持比例）", "style": "Heading2"},
        {"type": "text", "content": "width=200, height=100, keepAspectRatio=False, alignment=left"},
        {
            "type": "image",
            "path": "examples/demo.png",
            "width": 200,
            "height": 100,
            "alignment": "left",
            "keepAspectRatio": False
        },
        {"type": "spacer", "height": 0.5},

        # 右对齐 + 小尺寸
        {"type": "text", "content": "3. 右对齐（小尺寸）", "style": "Heading2"},
        {"type": "text", "content": "width=150, height=75, alignment=right"},
        {
            "type": "image",
            "path": "examples/demo.png",
            "width": 150,
            "height": 75,
            "alignment": "right",
            "keepAspectRatio": True
        },
        {"type": "spacer", "height": 0.5},

        # 大图展示
        {"type": "text", "content": "4. 全宽展示", "style": "Heading2"},
        {"type": "text", "content": "width=550, height=275, alignment=center"},
        {
            "type": "image",
            "path": "examples/demo.png",
            "width": 550,
            "height": 275,
            "alignment": "center",
            "keepAspectRatio": False
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/11_image.pdf")
print("✅ 已生成: examples/output/11_image.pdf")
