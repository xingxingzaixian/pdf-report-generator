# Python 库使用

## 基本用法

### 从配置字典生成

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "报告标题"},
    "elements": [
        {"type": "text", "content": "Hello World!", "style": "title"}
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output.pdf")
```

### 从配置文件生成

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_path="templates/sales_report.json")
generator.save("output.pdf")
```

### 获取字节流

```python
pdf_bytes = generator.to_bytes()
# pdf_bytes 是 bytes 类型，可以直接用于网络传输或进一步处理
```

## 动态添加数据

```python
import pandas as pd
from pdf_generator import PDFReportGenerator

# 准备数据
data = pd.DataFrame({
    "产品": ["A", "B", "C"],
    "销量": [100, 200, 150]
})

# 创建生成器并添加数据源
generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)
generator.save("output.pdf")
```

## 中文字体配置

```python
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=['./fonts', 'C:\\Windows\\Fonts']
)
generator.save("output.pdf")
```

## API 服务器启动

```python
from pdf_generator import start_api_server

start_api_server(host="localhost", port=8080)
```

## 下一步

- [配置结构总览](./configuration-overview.md) - 了解完整配置结构
- [Web API 使用](./usage-api.md) - 通过 HTTP API 生成 PDF
