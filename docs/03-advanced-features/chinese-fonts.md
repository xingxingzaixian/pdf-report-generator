# 中文字体配置

中文字体配置和使用完整指南。

## 📌 重要说明

**PDF Report Generator 不包含字体文件**，需要用户自己提供中文字体。这样设计的原因：
- 字体文件较大（每个 5-20 MB），避免增加包体积
- 不同用户可能需要不同的字体
- 避免字体许可证问题
- 可以使用系统已有的字体

## 🎯 支持的中文字体

系统会自动查找并注册以下中文字体：

| 字体名称 | 文件名 | 说明 |
|---------|--------|------|
| SimHei  | SimHei.ttf / SimHei.TTF / simhei.ttc | 黑体（推荐用于标题） |
| SimSun  | SimSun.ttf / SimSun.TTF / simsun.ttc | 宋体（推荐用于正文） |
| GB2312  | GB2312.ttf / GB2312.TTF | GB2312 编码字体 |

## 📂 字体查找顺序

系统会按以下顺序自动查找中文字体：

1. **用户指定的目录**（最高优先级）
2. **当前工作目录**下的 `fonts/` 目录
3. **用户主目录**下的 `.fonts/`、`fonts/`、`.local/share/fonts/` 目录

## 🔧 配置方式

### 方式 1：使用当前目录（最简单）

在项目根目录创建 `fonts/` 文件夹，放入字体文件：

```
your_project/
├── fonts/              # 创建这个目录
│   ├── SimHei.ttf     # 放入字体文件
│   ├── SimSun.ttf
│   └── ...
├── your_script.py
└── ...
```

代码中无需特殊配置：

```python
from pdf_generator import PDFReportGenerator

# 会自动查找当前目录下的 fonts/
generator = PDFReportGenerator(config_dict=config)
generator.generate('output.pdf')
```

### 方式 2：通过代码参数指定

```python
from pdf_generator import PDFReportGenerator

# 指定字体目录
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[
        './fonts',                    # 当前目录
        'C:\\Windows\\Fonts',         # Windows 系统字体
        '/usr/share/fonts/chinese',   # Linux 中文字体
    ]
)

generator.generate('output.pdf')
```

### 方式 3：在配置文件中指定

在 JSON 配置中添加 `fontDirs` 字段：

```json
{
  "metadata": {
    "title": "报告",
    "pageSize": "A4",
    "fontDirs": [
      "./fonts",
      "C:\\Windows\\Fonts"
    ]
  },
  "elements": [
    {
      "type": "text",
      "content": "中文内容"
    }
  ]
}
```

或者单个目录：

```json
{
  "metadata": {
    "title": "报告",
    "fontDirs": "./fonts"
  }
}
```

## 📥 获取字体文件

### Windows 用户

Windows 系统自带中文字体，位于：`C:\Windows\Fonts\`

**选项 1：直接使用系统字体**
```python
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['C:\\Windows\\Fonts']
)
```

**选项 2：复制到项目目录**
1. 打开 `C:\Windows\Fonts\`
2. 找到 `SimHei.ttf` 和 `SimSun.ttf`
3. 复制到项目的 `fonts/` 目录

### Mac 用户

Mac 系统字体位于：
- `/System/Library/Fonts/`
- `/Library/Fonts/`
- `~/Library/Fonts/`

可以使用系统字体或下载开源字体。

### Linux 用户

**安装中文字体包：**

```bash
# Ubuntu/Debian
sudo apt-get install fonts-wqy-microhei fonts-wqy-zenhei

# CentOS/RHEL
sudo yum install wqy-microhei-fonts wqy-zenhei-fonts
```

字体通常位于：
- `/usr/share/fonts/`
- `~/.local/share/fonts/`

**使用系统字体：**
```python
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['/usr/share/fonts']
)
```

### 下载开源字体

如果系统没有字体，可以下载开源字体：

1. **文泉驿微米黑**（推荐）
   - 官网：https://sourceforge.net/projects/wqy/
   - 开源免费，可商用

2. **思源黑体**
   - GitHub：https://github.com/adobe-fonts/source-han-sans
   - Adobe 开源字体，支持多语言

⚠️ **注意**：使用字体请确保遵守相应的许可证。

## 🎨 在样式中使用中文字体

### 基础使用

```json
{
  "styles": {
    "ChineseTitle": {
      "fontName": "SimHei",
      "fontSize": 18,
      "textColor": "#333333",
      "alignment": "center",
      "bold": true
    },
    "ChineseBody": {
      "fontName": "SimSun",
      "fontSize": 12,
      "alignment": "left"
    }
  },
  "elements": [
    {
      "type": "text",
      "content": "中文标题",
      "style": "ChineseTitle"
    },
    {
      "type": "text",
      "content": "这是正文内容...",
      "style": "ChineseBody"
    }
  ]
}
```

### 默认字体

如果成功加载了中文字体，系统会自动将以下样式的默认字体设置为中文字体：
- `Normal`
- `BodyText`
- `Title`
- `Heading1`
- `Heading2`

因此，即使不指定 `fontName`，中文也能正常显示：

```json
{
  "elements": [
    {
      "type": "text",
      "content": "这段中文会使用默认的中文字体",
      "style": "Normal"
    }
  ]
}
```

## 🔨 手动注册字体

如果需要使用特殊字体：

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict=config)

# 手动注册字体
generator.style_manager.register_font(
    'CustomFont',              # 字体名称
    '/path/to/CustomFont.ttf'  # 字体文件路径
)

# 在配置中使用
config = {
    "styles": {
        "custom": {
            "fontName": "CustomFont",
            "fontSize": 12
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
```

## 📊 Matplotlib 图表中文显示

系统自动配置 Matplotlib 使用中文字体，图表中的中文会正常显示：

```json
{
  "elements": [
    {
      "type": "chart",
      "chartType": "bar",
      "dataSource": "sales",
      "options": {
        "x": "产品",
        "y": "销量",
        "title": "产品销量对比",  
        "xlabel": "产品名称",
        "ylabel": "销量（件）"
      }
    }
  ]
}
```

图表中的标题、标签、图例等中文文字都会正确显示。

## ✅ 验证字体配置

### 检查已注册的字体

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict={})

# 查看已注册的字体
print("已注册的字体：", generator.style_manager.registered_fonts)
# 输出示例：{'SimHei', 'SimSun'}
```

### 测试字体显示

创建测试脚本：

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "字体测试"},
    "elements": [
        {
            "type": "text",
            "content": "中文字体测试：你好，世界！",
            "style": "Heading1"
        },
        {
            "type": "text",
            "content": "数字: 0123456789"
        },
        {
            "type": "text",
            "content": "English: Hello World"
        },
        {
            "type": "text",
            "content": "标点：，。！？；：""''（）"
        }
    ]
}

generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['./fonts']
)

print("已注册字体：", generator.style_manager.registered_fonts)
generator.generate('font_test.pdf')
print("测试完成，请检查 font_test.pdf")
```

## 🚨 常见问题

### Q: 中文显示为方框或乱码？

**原因：** 字体未正确加载

**解决方案：**
1. 确认字体文件存在于 `fonts/` 目录
2. 检查字体文件名是否正确（SimHei.ttf、SimSun.ttf）
3. 查看控制台输出，确认字体是否注册成功
4. 检查 `generator.style_manager.registered_fonts` 是否包含字体

### Q: 如何知道字体是否成功加载？

```python
generator = PDFReportGenerator(config_dict=config)
print(generator.style_manager.registered_fonts)
```

如果输出 `set()` 或空集合，说明没有加载到字体。

### Q: 可以不使用中文字体吗？

可以！如果不需要显示中文，系统会使用默认的英文字体（Helvetica），不会报错。

### Q: 支持其他格式的字体（如 .otf）吗？

ReportLab 主要支持 `.ttf` 和 `.ttc` 格式。`.otf` 格式支持有限，建议转换为 `.ttf`。

### Q: 打包后的应用如何处理字体？

**方案 1：要求用户提供**
在安装说明中注明：
```
请将中文字体文件放置在：
- Windows: C:\YourApp\fonts\
- Linux: ~/.yourapp/fonts/
```

**方案 2：与应用一起分发**（需注意许可证）
```python
import os
import sys

# 获取应用目录
if getattr(sys, 'frozen', False):
    # PyInstaller 打包后
    app_dir = sys._MEIPASS
else:
    app_dir = os.path.dirname(__file__)

font_dir = os.path.join(app_dir, 'fonts')

generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[font_dir]
)
```

## 📝 完整示例

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 准备数据
data = pd.DataFrame({
    "产品": ["产品A", "产品B", "产品C"],
    "销量": [100, 150, 200],
    "收入": [10000, 15000, 20000]
})

# 配置（包含字体设置）
config = {
    "metadata": {
        "title": "销售报告",
        "pageSize": "A4",
        "fontDirs": ["./fonts"]  # 字体目录
    },
    "styles": {
        "title": {
            "fontName": "SimHei",
            "fontSize": 20,
            "alignment": "center"
        },
        "body": {
            "fontName": "SimSun",
            "fontSize": 12
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "2024年销售报告",
            "style": "title"
        },
        {
            "type": "table",
            "dataSource": "sales"
        },
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "options": {
                "x": "产品",
                "y": "销量",
                "title": "产品销量对比"
            }
        }
    ]
}

# 生成 PDF
generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)

# 查看加载的字体
print("已加载字体：", generator.style_manager.registered_fonts)

# 生成报告
generator.generate('sales_report.pdf')
print("✅ 报告生成完成！")
```

## 🎓 最佳实践

1. **开发环境**：使用项目本地的 `fonts/` 目录
2. **生产环境**：从配置文件读取字体路径
3. **文档说明**：在 README 中注明所需字体及获取方式
4. **降级策略**：即使没有中文字体，也能生成 PDF（英文部分正常）
5. **字体选择**：
   - 标题使用黑体（SimHei）- 醒目
   - 正文使用宋体（SimSun）- 易读

## 📚 相关文档

- [安装指南](../01-getting-started/installation.md) - 安装配置
- [配置概述](../02-user-guide/configuration-overview.md) - 配置说明
- [样式配置](../02-user-guide/styles.md) - 样式详解
- [字体配置指南](../../FONT_CONFIGURATION.md) - 根目录详细说明

---

**上一页**：[表格合并](./table-merging.md)  
**下一页**：[图片处理](./images-handling.md)

