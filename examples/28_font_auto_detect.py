"""
28 - 字体：自动检测 + 指定目录

演示字体配置的三种方式：
1. 自动检测（项目 fonts/ 目录）
2. 通过 font_dirs 参数指定
3. 在配置文件中指定 fontDirs
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

# === 方式1: 自动检测 ===
print("方式1: 自动检测 fonts/ 目录")

config1 = {
    "metadata": {"title": "字体 - 自动检测"},
    "elements": [
        {"type": "text", "content": "自动检测字体", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "系统自动从 fonts/ 目录加载中文字体。"},
        {"type": "text", "content": "中文测试：你好世界！这是中文字体测试。"},
        {"type": "text", "content": "数字测试：0123456789"},
        {"type": "text", "content": "混合测试：中文English数字123标点！"},
    ]
}

gen1 = PDFReportGenerator(config_dict=config1)
fonts = gen1.style_manager.registered_fonts if hasattr(gen1.style_manager, 'registered_fonts') else []
print(f"  已注册字体: {fonts}")
gen1.save("examples/output/28_font_auto_a.pdf")

# === 方式2: 指定字体目录 ===
print("方式2: 通过 font_dirs 参数指定")

font_dirs = ['./fonts']
if os.name == 'nt':
    font_dirs.append('C:\\Windows\\Fonts')
else:
    font_dirs.append('/usr/share/fonts')

config2 = {
    "metadata": {"title": "字体 - 指定目录"},
    "elements": [
        {"type": "text", "content": "指定字体目录", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": f"搜索目录: {font_dirs}"},
        {"type": "text", "content": "通过 font_dirs 参数指定字体搜索路径。"},
        {"type": "text", "content": "中文测试：你好世界！"},
    ]
}

gen2 = PDFReportGenerator(config_dict=config2, font_dirs=font_dirs)
fonts2 = gen2.style_manager.registered_fonts if hasattr(gen2.style_manager, 'registered_fonts') else []
print(f"  已注册字体: {fonts2}")
gen2.save("examples/output/28_font_auto_b.pdf")

# === 方式3: 配置文件中指定 ===
print("方式3: 在配置文件中指定 fontDirs")

config3 = {
    "metadata": {
        "title": "字体 - 配置文件指定",
        "fontDirs": ["./fonts"]
    },
    "elements": [
        {"type": "text", "content": "配置文件指定字体", "style": "Title"},
        {"type": "text", "content": "在 metadata.fontDirs 中指定字体目录。"},
        {"type": "text", "content": "中文测试：你好世界！"},
    ]
}

gen3 = PDFReportGenerator(config_dict=config3)
gen3.save("examples/output/28_font_auto_c.pdf")

print("✅ 已生成: examples/output/28_font_auto_a.pdf")
print("✅ 已生成: examples/output/28_font_auto_b.pdf")
print("✅ 已生成: examples/output/28_font_auto_c.pdf")
