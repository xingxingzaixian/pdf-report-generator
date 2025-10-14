"""
字体配置示例

演示如何配置和使用中文字体
"""

from pdf_generator import PDFReportGenerator
import os


def example_1_auto_detect():
    """示例 1: 自动检测字体（当前目录 fonts/）"""
    print("\n=== 示例 1: 自动检测字体 ===")
    
    config = {
        "document": {
            "title": "自动检测字体示例",
            "pageSize": "A4"
        },
        "content": [
            {
                "type": "text",
                "content": "自动检测字体示例",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "这段文字会使用自动检测到的中文字体。",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "如果当前目录有 fonts/ 文件夹，系统会自动加载其中的字体。"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    print(f"已注册字体: {generator.style_manager.registered_fonts}")
    
    generator.generate("font_example_01_auto.pdf")
    print("✅ 已生成: font_example_01_auto.pdf")


def example_2_specify_dirs():
    """示例 2: 指定字体目录"""
    print("\n=== 示例 2: 指定字体目录 ===")
    
    config = {
        "document": {
            "title": "指定字体目录示例"
        },
        "content": [
            {
                "type": "text",
                "content": "指定字体目录示例",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "通过 font_dirs 参数指定字体位置"
            }
        ]
    }
    
    # 指定多个字体目录
    font_dirs = [
        './fonts',                    # 当前目录
        os.path.expanduser('~/fonts'), # 用户目录
    ]
    
    # Windows 用户可以添加系统字体目录
    if os.name == 'nt':
        font_dirs.append('C:\\Windows\\Fonts')
    
    generator = PDFReportGenerator(
        config_dict=config,
        font_dirs=font_dirs
    )
    
    print(f"搜索目录: {font_dirs}")
    print(f"已注册字体: {generator.style_manager.registered_fonts}")
    
    generator.generate("font_example_02_dirs.pdf")
    print("✅ 已生成: font_example_02_dirs.pdf")


def example_3_config_file():
    """示例 3: 在配置文件中指定字体"""
    print("\n=== 示例 3: 配置文件中指定字体 ===")
    
    config = {
        "document": {
            "title": "配置文件字体示例",
            "fontDirs": ["./fonts", "/usr/share/fonts"]  # 在配置中指定
        },
        "content": [
            {
                "type": "text",
                "content": "配置文件中指定字体",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "字体目录在 JSON 配置的 document.fontDirs 中定义"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    print(f"已注册字体: {generator.style_manager.registered_fonts}")
    
    generator.generate("font_example_03_config.pdf")
    print("✅ 已生成: font_example_03_config.pdf")


def example_4_custom_font():
    """示例 4: 手动注册自定义字体"""
    print("\n=== 示例 4: 手动注册自定义字体 ===")
    
    config = {
        "document": {"title": "自定义字体示例"},
        "styles": {
            "customFont": {
                "fontName": "MyCustomFont",  # 使用自定义字体
                "fontSize": 14,
                "textColor": "#0066CC"
            }
        },
        "content": [
            {
                "type": "text",
                "content": "使用自定义字体",
                "style": "customFont"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    
    # 手动注册字体（假设有这个字体文件）
    custom_font_path = "./fonts/CustomFont.ttf"
    if os.path.exists(custom_font_path):
        generator.style_manager.register_font(
            'MyCustomFont',
            custom_font_path
        )
        print(f"✅ 已注册自定义字体: MyCustomFont")
    else:
        print(f"⚠️  字体文件不存在: {custom_font_path}")
        print("    将使用默认字体")
    
    print(f"已注册字体: {generator.style_manager.registered_fonts}")
    
    generator.generate("font_example_04_custom.pdf")
    print("✅ 已生成: font_example_04_custom.pdf")


def example_5_test_fonts():
    """示例 5: 测试字体显示"""
    print("\n=== 示例 5: 字体测试 ===")
    
    config = {
        "document": {
            "title": "字体测试"
        },
        "content": [
            {
                "type": "text",
                "content": "字体测试报告",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "中文测试：你好世界！这是中文字体测试。",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "English Test: Hello World! This is English font test.",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "数字测试：0123456789",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "标点符号：，。！？；：""''（）【】",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "混合内容：中文English数字123标点！",
                "style": "Normal"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    
    print("\n字体信息:")
    print(f"  已注册字体: {generator.style_manager.registered_fonts}")
    print(f"  字体数量: {len(generator.style_manager.registered_fonts)}")
    
    if generator.style_manager.registered_fonts:
        print("  ✅ 中文字体已加载，中文应该可以正常显示")
    else:
        print("  ⚠️  未找到中文字体，中文可能显示为方框")
        print("     请检查字体配置（参考 FONT_CONFIGURATION.md）")
    
    generator.generate("font_example_05_test.pdf")
    print("\n✅ 已生成: font_example_05_test.pdf")
    print("   请打开 PDF 检查字体显示效果")


def show_font_info():
    """显示字体查找信息"""
    print("\n" + "=" * 70)
    print("字体配置信息")
    print("=" * 70)
    
    from pathlib import Path
    
    print("\n字体查找顺序:")
    print("  1. 用户指定目录（通过 font_dirs 参数）")
    print("  2. 当前工作目录的 fonts/ 子目录")
    print("  3. 用户主目录的 .fonts/ 或 fonts/ 目录")
    
    print("\n当前环境:")
    print(f"  当前工作目录: {Path.cwd()}")
    print(f"  用户主目录: {Path.home()}")
    
    # 检查常见位置
    print("\n检查常见字体位置:")
    
    paths_to_check = [
        Path.cwd() / "fonts",
        Path.home() / ".fonts",
        Path.home() / "fonts",
    ]
    
    if os.name == 'nt':  # Windows
        paths_to_check.append(Path("C:/Windows/Fonts"))
    else:  # Linux/Mac
        paths_to_check.extend([
            Path("/usr/share/fonts"),
            Path.home() / ".local/share/fonts"
        ])
    
    for path in paths_to_check:
        exists = "✅" if path.exists() else "❌"
        print(f"  {exists} {path}")


def main():
    """运行所有示例"""
    print("=" * 70)
    print("PDF Report Generator - 字体配置示例")
    print("=" * 70)
    
    show_font_info()
    
    try:
        example_1_auto_detect()
        example_2_specify_dirs()
        example_3_config_file()
        example_4_custom_font()
        example_5_test_fonts()
        
        print("\n" + "=" * 70)
        print("所有示例完成！")
        print("=" * 70)
        print("\n提示:")
        print("  - 如果中文显示有问题，请参考 FONT_CONFIGURATION.md")
        print("  - 将字体文件放在项目的 fonts/ 目录下")
        print("  - 或指定系统字体目录")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

