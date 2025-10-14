# 字体配置示例

中文字体配置的完整示例集合。

## 示例 1：基础字体配置

### 项目结构
```
my_project/
├── fonts/                    # 字体目录
│   ├── SimHei.ttf           # 黑体
│   └── SimSun.ttf           # 宋体
├── config/
│   └── report.json          # 配置文件
└── generate_report.py       # 生成脚本
```

### 配置文件 (config/report.json)
```json
{
  "metadata": {
    "title": "销售报告",
    "pageSize": "A4"
  },
  "styles": {
    "title": {
      "fontName": "SimHei",
      "fontSize": 20,
      "alignment": "center",
      "textColor": "#333333"
    },
    "body": {
      "fontName": "SimSun",
      "fontSize": 12,
      "alignment": "left"
    }
  },
  "elements": [
    {
      "type": "text",
      "content": "2024年销售报告",
      "style": "title"
    },
    {
      "type": "text",
      "content": "本报告总结了2024年的销售业绩和市场表现。",
      "style": "body"
    }
  ]
}
```

### 生成脚本 (generate_report.py)
```python
from pdf_generator import PDFReportGenerator
import json

# 读取配置
with open('config/report.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# 生成 PDF（自动查找 fonts/ 目录）
generator = PDFReportGenerator(config_dict=config)

# 验证字体加载
print("已注册字体：", generator.style_manager.registered_fonts)

# 生成报告
generator.generate('output/sales_report.pdf')
print("✅ 报告生成完成！")
```

## 示例 2：多目录字体配置

### 代码示例
```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "多字体测试"},
    "elements": [
        {"type": "text", "content": "测试中文字体显示"}
    ]
}

# 指定多个字体目录
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[
        './fonts',                    # 项目字体
        'C:\\Windows\\Fonts',         # Windows 系统字体
        '/usr/share/fonts/chinese',   # Linux 中文字体
        '~/.fonts',                   # 用户字体
    ]
)

print("搜索目录：", [
    './fonts',
    'C:\\Windows\\Fonts',
    '/usr/share/fonts/chinese',
    '~/.fonts'
])
print("已注册字体：", generator.style_manager.registered_fonts)

generator.generate('multi_font_test.pdf')
```

## 示例 3：配置文件指定字体

### 配置文件
```json
{
  "metadata": {
    "title": "配置指定字体",
    "pageSize": "A4",
    "fontDirs": [
      "./fonts",
      "C:\\Windows\\Fonts"
    ]
  },
  "elements": [
    {
      "type": "text",
      "content": "这个配置在 JSON 中指定了字体目录"
    }
  ]
}
```

### 生成代码
```python
from pdf_generator import PDFReportGenerator

# 从配置文件加载（包含字体目录）
generator = PDFReportGenerator(config_path='config_with_fonts.json')

print("已注册字体：", generator.style_manager.registered_fonts)
generator.generate('config_font_test.pdf')
```

## 示例 4：手动注册字体

### 代码示例
```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "自定义字体测试"},
    "styles": {
        "custom": {
            "fontName": "MyCustomFont",
            "fontSize": 14
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "使用自定义字体",
            "style": "custom"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)

# 手动注册字体
custom_font_path = "./fonts/CustomFont.ttf"
if os.path.exists(custom_font_path):
    generator.style_manager.register_font(
        'MyCustomFont',
        custom_font_path
    )
    print("✅ 自定义字体注册成功")
else:
    print("⚠️ 自定义字体文件不存在")

print("已注册字体：", generator.style_manager.registered_fonts)
generator.generate('custom_font_test.pdf')
```

## 示例 5：字体测试报告

### 完整测试脚本
```python
from pdf_generator import PDFReportGenerator
import os

def test_fonts():
    """测试字体配置和显示效果"""
    
    config = {
        "metadata": {
            "title": "字体测试报告"
        },
        "elements": [
            {
                "type": "text",
                "content": "字体测试报告",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "中文字体测试：你好，世界！",
                "style": "Normal"
            },
            {
                "type": "text",
                "content": "English Test: Hello World!",
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
    
    # 创建生成器
    generator = PDFReportGenerator(config_dict=config)
    
    # 显示字体信息
    print("\n字体配置信息:")
    print(f"  已注册字体: {generator.style_manager.registered_fonts}")
    print(f"  字体数量: {len(generator.style_manager.registered_fonts)}")
    
    if generator.style_manager.registered_fonts:
        print("  ✅ 中文字体已加载，中文应该可以正常显示")
    else:
        print("  ⚠️ 未找到中文字体，中文可能显示为方框")
        print("     请检查字体配置（参考 docs/03-advanced-features/chinese-fonts.md）")
    
    # 生成测试报告
    output_file = "font_test_report.pdf"
    generator.generate(output_file)
    print(f"\n✅ 测试报告已生成: {output_file}")
    print("   请打开 PDF 检查字体显示效果")

if __name__ == "__main__":
    test_fonts()
```

## 示例 6：不同平台的字体配置

### Windows 配置
```python
from pdf_generator import PDFReportGenerator

# Windows 使用系统字体
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['C:\\Windows\\Fonts']
)
```

### Linux 配置
```python
from pdf_generator import PDFReportGenerator

# Linux 使用系统字体
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['/usr/share/fonts', '~/.local/share/fonts']
)
```

### Mac 配置
```python
from pdf_generator import PDFReportGenerator

# Mac 使用系统字体
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['/System/Library/Fonts', '~/Library/Fonts']
)
```

### 跨平台配置
```python
import os
from pdf_generator import PDFReportGenerator

def get_system_font_dirs():
    """获取系统字体目录"""
    font_dirs = []
    
    if os.name == 'nt':  # Windows
        font_dirs.append('C:\\Windows\\Fonts')
    elif os.name == 'posix':  # Linux/Mac
        font_dirs.extend([
            '/usr/share/fonts',
            '~/.local/share/fonts',
            '/System/Library/Fonts',  # Mac
            '~/Library/Fonts'         # Mac
        ])
    
    return font_dirs

# 使用系统字体目录
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=get_system_font_dirs()
)
```

## 示例 7：字体配置验证工具

### 验证脚本
```python
from pdf_generator import PDFReportGenerator
from pathlib import Path

def validate_font_config():
    """验证字体配置"""
    
    print("🔍 字体配置验证工具")
    print("=" * 50)
    
    # 检查常见字体目录
    font_dirs_to_check = [
        './fonts',
        'C:\\Windows\\Fonts',
        '/usr/share/fonts',
        '~/.fonts',
        '~/.local/share/fonts'
    ]
    
    print("\n📂 检查字体目录:")
    existing_dirs = []
    for font_dir in font_dirs_to_check:
        path = Path(font_dir).expanduser()
        if path.exists():
            print(f"  ✅ {font_dir}")
            existing_dirs.append(str(path))
        else:
            print(f"  ❌ {font_dir}")
    
    # 测试字体加载
    print("\n🔤 测试字体加载:")
    generator = PDFReportGenerator(config_dict={})
    
    if generator.style_manager.registered_fonts:
        print(f"  ✅ 成功加载字体: {generator.style_manager.registered_fonts}")
    else:
        print("  ❌ 未加载任何字体")
    
    # 生成测试报告
    print("\n📄 生成测试报告:")
    test_config = {
        "metadata": {"title": "字体验证报告"},
        "elements": [
            {"type": "text", "content": "字体验证测试：你好世界！"}
        ]
    }
    
    generator = PDFReportGenerator(config_dict=test_config)
    generator.generate('font_validation_report.pdf')
    print("  ✅ 测试报告已生成: font_validation_report.pdf")
    
    # 建议
    print("\n💡 建议:")
    if not generator.style_manager.registered_fonts:
        print("  1. 在项目目录创建 fonts/ 文件夹")
        print("  2. 将中文字体文件放入该文件夹")
        print("  3. 或指定系统字体目录")
    else:
        print("  ✅ 字体配置正常，可以正常显示中文")

if __name__ == "__main__":
    validate_font_config()
```

## 运行示例

### 运行所有示例
```bash
# 创建示例目录
mkdir -p examples/font_examples
cd examples/font_examples

# 创建字体目录
mkdir fonts

# 复制字体文件到 fonts/ 目录
# Windows: copy C:\Windows\Fonts\SimHei.ttf fonts\
# Linux: sudo cp /usr/share/fonts/truetype/wqy/wqy-microhei.ttc fonts/SimHei.ttf

# 运行示例
python font_configuration_examples.py
```

## 相关文档

- [中文字体配置完整指南](../03-advanced-features/chinese-fonts.md)
- [字体配置快速参考](../03-advanced-features/font-quick-reference.md)
- [字体配置指南](../../FONT_CONFIGURATION.md)
- [安装指南](../01-getting-started/installation.md)

---

**上一页**：[字体配置快速参考](../03-advanced-features/font-quick-reference.md)  
**下一页**：[其他示例](./other-examples.md)
