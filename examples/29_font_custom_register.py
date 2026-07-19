"""
29 - 字体：手动注册 + 多字体混用 + 指定字体名称

演示三种使用自定义字体的方式：
1. 手动注册字体并指定自定义名称
2. 在样式中通过 fontName 使用已注册字体
3. 多种字体混合使用（不同元素用不同字体）
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# ============================================================
# 方式1: 手动注册单个字体并指定自定义名称
# ============================================================
print("=" * 60)
print("方式1: 手动注册字体，指定自定义名称")
print("=" * 60)

config1 = {
    "metadata": {"title": "手动注册字体 - 黑体"},
    "styles": {
        # 在样式中通过 fontName 指定使用哪个字体
        "heiTitle": {
            "fontName": "MySimHei",       # 使用手动注册的字体
            "fontSize": 22,
            "textColor": "#2C3E50",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 15
        },
        "heiBody": {
            "fontName": "MySimHei",
            "fontSize": 12,
            "textColor": "#34495E",
            "spaceAfter": 8
        },
        "heiHighlight": {
            "fontName": "MySimHei",
            "fontSize": 14,
            "textColor": "#E74C3C",
            "bold": True,
            "spaceAfter": 8
        }
    },
    "elements": [
        {"type": "text", "content": "黑体字体演示（SimHei）", "style": "heiTitle"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "这段文字使用手动注册的 SimHei（黑体）字体。", "style": "heiBody"},
        {"type": "text", "content": "黑体笔画粗壮，适合标题使用。", "style": "heiHighlight"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "注册方式:", "style": "Heading2"},
        {"type": "text", "content": "  generator.style_manager.register_font('MySimHei', 'fonts/SimHei.TTF')"},
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)

# 手动注册字体
font_path = "fonts/SimHei.TTF"
if os.path.exists(font_path):
    gen1.style_manager.register_font("MySimHei", font_path)
    print(f"  ✅ 已注册: MySimHei → {font_path}")
else:
    print(f"  ⚠️  字体文件不存在: {font_path}")

gen1.save("examples/output/29_font_custom_a.pdf")
print("  ✅ 已生成: examples/output/29_font_custom_a.pdf")
print()


# ============================================================
# 方式2: 手动注册多个字体，混用不同字体
# ============================================================
print("=" * 60)
print("方式2: 注册多个字体，不同元素用不同字体")
print("=" * 60)

config2 = {
    "metadata": {"title": "多字体混用演示"},
    "styles": {
        "songTitle": {
            "fontName": "MySimSun",       # 宋体 - 标题
            "fontSize": 20,
            "textColor": "#1A5490",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 12
        },
        "heiSection": {
            "fontName": "MySimHei",       # 黑体 - 章节标题
            "fontSize": 14,
            "textColor": "#2C3E50",
            "bold": True,
            "spaceBefore": 10,
            "spaceAfter": 5
        },
        "songBody": {
            "fontName": "MySimSun",       # 宋体 - 正文
            "fontSize": 11,
            "textColor": "#333333",
            "spaceAfter": 6
        },
        "gbNote": {
            "fontName": "MyGB2312",       # GB2312 - 注释
            "fontSize": 9,
            "textColor": "#7F8C8D",
            "spaceAfter": 4
        }
    },
    "elements": [
        {"type": "text", "content": "多字体混用演示报告", "style": "songTitle"},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "一、字体说明", "style": "heiSection"},
        {"type": "text", "content": "本报告使用三种不同的中文字体：", "style": "songBody"},
        {"type": "text", "content": "• 宋体（SimSun）— 用于标题和正文，笔画纤细，适合长文阅读。", "style": "songBody"},
        {"type": "text", "content": "• 黑体（SimHei）— 用于章节标题，笔画粗壮，醒目突出。", "style": "songBody"},
        {"type": "text", "content": "• GB2312 — 用于注释信息，等宽风格。", "style": "songBody"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "二、中文文本展示", "style": "heiSection"},
        {"type": "text", "content": "你好世界！这是一段使用宋体渲染的中文正文。宋体是印刷中最常用的字体之一，适合大段文字的排版。", "style": "songBody"},
        {"type": "text", "content": "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。", "style": "songBody"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "三、特殊字符测试", "style": "heiSection"},
        {"type": "text", "content": "标点符号：，。！？；：""''（）【】《》", "style": "songBody"},
        {"type": "text", "content": "数学符号：± × ÷ ≠ ≤ ≥ √ ∞ ∑", "style": "songBody"},
        {"type": "text", "content": "货币符号：¥ $ € £ ₩ ₹", "style": "songBody"},
        {"type": "text", "content": "中英混排：产品 Product-A 销量 1,200 units", "style": "songBody"},
        {"type": "spacer", "height": 0.2},

        {"type": "text", "content": "注释：本报告由 PDF Report Generator 自动生成", "style": "gbNote"},
        {"type": "text", "content": "字体文件来源：fonts/SimSun.TTF, fonts/SimHei.TTF, fonts/GB2312.TTF", "style": "gbNote"},
    ]
}

gen2 = PDFReportGenerator(config_dict=config2)

# 注册多个字体
fonts_to_register = {
    "MySimSun": "fonts/SimSun.TTF",
    "MySimHei": "fonts/SimHei.TTF",
    "MyGB2312": "fonts/GB2312.TTF",
}

for name, path in fonts_to_register.items():
    if os.path.exists(path):
        gen2.style_manager.register_font(name, path)
        print(f"  ✅ 已注册: {name} → {path}")
    else:
        print(f"  ⚠️  字体文件不存在: {path}")

gen2.save("examples/output/29_font_custom_b.pdf")
print("  ✅ 已生成: examples/output/29_font_custom_b.pdf")
print()


# ============================================================
# 方式3: 手动注册 + 自动检测混用
# ============================================================
print("=" * 60)
print("方式3: 手动注册字体 + 自动检测字体混用")
print("=" * 60)

config3 = {
    "metadata": {"title": "手动+自动字体混用"},
    "styles": {
        "customTitle": {
            "fontName": "MyCustomSimHei",     # 手动注册的字体
            "fontSize": 22,
            "textColor": "#8E44AD",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 15
        },
        "autoBody": {
            # 不指定 fontName，使用自动检测的字体
            "fontSize": 11,
            "textColor": "#333333",
            "spaceAfter": 6
        }
    },
    "elements": [
        {"type": "text", "content": "手动+自动字体混用", "style": "customTitle"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "标题使用手动注册的 MyCustomSimHei 字体（紫色）。", "style": "autoBody"},
        {"type": "text", "content": "正文使用系统自动检测到的字体（黑色）。", "style": "autoBody"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "这种混用方式适合以下场景：", "style": "Heading2"},
        {"type": "text", "content": "1. 标题需要特殊的品牌字体"},
        {"type": "text", "content": "2. 正文使用系统默认字体即可"},
        {"type": "text", "content": "3. 特殊符号需要专门的字体支持"},
    ]
}

gen3 = PDFReportGenerator(config_dict=config3)

# 手动注册一个自定义名称的字体（与自动检测的字体共存）
custom_font_path = "fonts/SimHei.TTF"
if os.path.exists(custom_font_path):
    gen3.style_manager.register_font("MyCustomSimHei", custom_font_path)
    print(f"  ✅ 已注册: MyCustomSimHei → {custom_font_path}")

# 显示所有已注册字体
if hasattr(gen3.style_manager, 'registered_fonts'):
    fonts = gen3.style_manager.registered_fonts
    print(f"  所有已注册字体: {fonts}")
    print(f"  字体数量: {len(fonts)}")

gen3.save("examples/output/29_font_custom_c.pdf")
print("  ✅ 已生成: examples/output/29_font_custom_c.pdf")
print()


print("=" * 60)
print("总结: register_font() 使用方式")
print("=" * 60)
print("  generator = PDFReportGenerator(config_dict=config)")
print("  generator.style_manager.register_font('自定义名称', '字体文件路径')")
print()
print("  然后在样式中通过 fontName 使用:")
print('  "myStyle": {"fontName": "自定义名称", "fontSize": 12}')
