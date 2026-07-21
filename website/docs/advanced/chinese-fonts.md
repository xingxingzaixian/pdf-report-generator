# 中文字体

PDF Report Generator 支持自动检测和加载中文字体。

## 自动检测

系统会自动搜索以下目录中的中文字体：

- 项目 `fonts/` 目录
- 系统字体目录（Windows / macOS / Linux）

## 手动指定字体目录

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[
        './fonts',
        '/System/Library/Fonts',           # macOS
        'C:\\Windows\\Fonts',              # Windows
        '/usr/share/fonts'                 # Linux
    ]
)
generator.save("output.pdf")
```

## 在配置中指定字体

```json
{
  "styles": {
    "chineseTitle": {
      "fontName": "SimSun",
      "fontSize": 24,
      "alignment": "center"
    }
  }
}
```

## 常见中文字体

| 字体名称 | 说明 |
|----------|------|
| SimSun | 宋体 |
| SimHei | 黑体 |
| Microsoft YaHei | 微软雅黑 |
| PingFang SC | 苹方（macOS） |
| STSong | 华文宋体 |
| STHeiti | 华文黑体 |

## 注册自定义字体

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 注册字体
pdfmetrics.registerFont(TTFont('MyChineseFont', 'fonts/my-font.ttf'))

# 在配置中使用
config = {
    "styles": {
        "customChinese": {
            "fontName": "MyChineseFont",
            "fontSize": 12
        }
    }
}
```

## 常见问题

### 中文显示为方块

- 确认字体目录中包含中文字体
- 尝试手动指定字体目录
- 使用 `font_dirs` 参数明确指定

### 字体加载失败

- 检查字体文件是否完整
- 确认文件权限
- 尝试使用系统自带字体

## 下一步

- [样式系统](/guide/styles.md) - 了解样式配置
- [条件渲染](./conditional-rendering.md) - 根据条件显示内容
