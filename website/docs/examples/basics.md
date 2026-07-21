# 基础示例

## Hello PDF

最简单的 PDF 生成示例：

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "Hello PDF"},
    "elements": [
        {
            "type": "text",
            "content": "Hello PDF Report Generator!",
            "style": "title"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/hello.pdf")
```

## 文本样式

使用不同的文本样式：

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "文本样式示例"},
    "styles": {
        "title": {"fontSize": 24, "alignment": "center", "bold": true},
        "subtitle": {"fontSize": 16, "textColor": "#666666"},
        "body": {"fontSize": 12, "textColor": "#333333"},
        "highlight": {"fontSize": 14, "textColor": "#4472C4", "bold": true}
    },
    "elements": [
        {"type": "text", "content": "主标题", "style": "title"},
        {"type": "text", "content": "副标题", "style": "subtitle"},
        {"type": "spacer", "height": 0.5},
        {"type": "text", "content": "这是正文内容，使用默认样式。", "style": "body"},
        {"type": "text", "content": "这是高亮文本。", "style": "highlight"}
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/text_styles.pdf")
```

## 简单表格

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "表格示例"},
    "elements": [
        {"type": "text", "content": "产品列表", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "table",
            "dataSource": "products",
            "columns": ["产品", "价格", "库存"]
        }
    ]
}

data = [
    {"产品": "产品A", "价格": 99, "库存": 100},
    {"产品": "产品B", "价格": 199, "库存": 50},
    {"产品": "产品C", "价格": 299, "库存": 30}
]

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("products", data)
generator.save("output/simple_table.pdf")
```

## 图片插入

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "图片示例"},
    "elements": [
        {"type": "text", "content": "图片展示", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "image",
            "path": "images/demo.png",
            "width": 400,
            "alignment": "center"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/image_example.pdf")
```

## 分页控制

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "分页示例"},
    "elements": [
        {"type": "text", "content": "第一页内容", "style": "title"},
        {"type": "text", "content": "这里有一些内容..."},
        {"type": "pagebreak"},
        {"type": "text", "content": "第二页内容", "style": "title"},
        {"type": "text", "content": "分页后的内容..."}
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/page_break.pdf")
```
