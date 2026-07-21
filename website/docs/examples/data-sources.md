# 数据源示例

## CSV 数据

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "CSV 数据示例"},
    "dataSources": [
        {
            "name": "csv_data",
            "type": "csv",
            "path": "data/sales.csv"
        }
    ],
    "elements": [
        {"type": "text", "content": "CSV 数据展示", "style": "title"},
        {
            "type": "table",
            "dataSource": "csv_data",
            "columns": ["产品", "销量", "金额"]
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/csv_data.pdf")
```

## JSON 数据

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "JSON 数据示例"},
    "dataSources": [
        {
            "name": "json_data",
            "type": "json",
            "path": "data/report.json"
        }
    ],
    "elements": [
        {"type": "text", "content": "JSON 数据展示", "style": "title"},
        {
            "type": "table",
            "dataSource": "json_data"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/json_data.pdf")
```

## Excel 数据

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "Excel 数据示例"},
    "dataSources": [
        {
            "name": "excel_data",
            "type": "excel",
            "path": "data/report.xlsx",
            "sheet": "Sheet1"
        }
    ],
    "elements": [
        {"type": "text", "content": "Excel 数据展示", "style": "title"},
        {
            "type": "table",
            "dataSource": "excel_data"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/excel_data.pdf")
```

## DataFrame 数据

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 创建 DataFrame
data = pd.DataFrame({
    "产品": ["A", "B", "C", "D"],
    "销量": [150, 230, 180, 310],
    "金额": [45000, 69000, 54000, 93000]
})

config = {
    "metadata": {"title": "DataFrame 示例"},
    "elements": [
        {"type": "text", "content": "DataFrame 数据展示", "style": "title"},
        {
            "type": "table",
            "dataSource": "sales"
        },
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销量"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)
generator.save("output/dataframe.pdf")
```

## API 数据

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "API 数据示例"},
    "dataSources": [
        {
            "name": "api_data",
            "type": "api",
            "url": "https://jsonplaceholder.typicode.com/posts",
            "method": "GET"
        }
    ],
    "elements": [
        {"type": "text", "content": "API 数据展示", "style": "title"},
        {
            "type": "table",
            "dataSource": "api_data",
            "columns": ["userId", "id", "title"]
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output/api_data.pdf")
```
