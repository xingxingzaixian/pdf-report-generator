# Pipeline 示例

## 数据过滤

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

data = pd.DataFrame({
    "产品": ["A", "B", "C", "D", "E"],
    "销量": [100, 250, 80, 320, 150],
    "类别": ["电子", "电子", "食品", "电子", "食品"]
})

config = {
    "metadata": {"title": "过滤示例"},
    "dataSources": [
        {
            "name": "raw_data",
            "type": "csv",
            "path": "data/products.csv"
        }
    ],
    "pipeline": [
        {
            "name": "high_sales",
            "type": "filter",
            "source": "raw_data",
            "condition": "销量 > 150"
        }
    ],
    "elements": [
        {"type": "text", "content": "高销量产品", "style": "title"},
        {
            "type": "table",
            "dataSource": "high_sales"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("raw_data", data)
generator.save("output/pipeline_filter.pdf")
```

## 数据转换

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

data = pd.DataFrame({
    "产品": ["A", "B", "C"],
    "销量": [100, 200, 150],
    "单价": [50, 30, 40]
})

config = {
    "metadata": {"title": "转换示例"},
    "pipeline": [
        {
            "name": "with_revenue",
            "type": "transform",
            "source": "raw_data",
            "mappings": {
                "金额": "销量 * 单价"
            }
        }
    ],
    "elements": [
        {"type": "text", "content": "销售数据", "style": "title"},
        {
            "type": "table",
            "dataSource": "with_revenue",
            "columns": ["产品", "销量", "单价", "金额"]
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("raw_data", data)
generator.save("output/pipeline_transform.pdf")
```

## 数据聚合

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

data = pd.DataFrame({
    "类别": ["电子", "电子", "食品", "食品", "服装", "服装"],
    "销量": [100, 150, 80, 120, 90, 110]
})

config = {
    "metadata": {"title": "聚合示例"},
    "pipeline": [
        {
            "name": "category_summary",
            "type": "aggregate",
            "source": "raw_data",
            "groupBy": "类别",
            "aggregations": {
                "total_sales": "sum(销量)",
                "avg_sales": "avg(销量)",
                "count": "count()"
            }
        }
    ],
    "elements": [
        {"type": "text", "content": "分类汇总", "style": "title"},
        {
            "type": "table",
            "dataSource": "category_summary"
        },
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "category_summary",
            "xAxis": "类别",
            "yAxis": "total_sales",
            "title": "各品类销量"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("raw_data", data)
generator.save("output/pipeline_aggregate.pdf")
```

## 完整工作流

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

data = pd.DataFrame({
    "日期": ["2024-01", "2024-01", "2024-02", "2024-02"],
    "产品": ["A", "B", "A", "B"],
    "类别": ["电子", "食品", "电子", "食品"],
    "销量": [100, 150, 120, 180],
    "金额": [5000, 4500, 6000, 5400]
})

config = {
    "metadata": {"title": "完整工作流示例"},
    "pipeline": [
        {
            "name": "electronics",
            "type": "filter",
            "source": "raw_data",
            "condition": "类别 == '电子'"
        },
        {
            "name": "monthly_summary",
            "type": "aggregate",
            "source": "electronics",
            "groupBy": "日期",
            "aggregations": {
                "total_amount": "sum(金额)",
                "total_sales": "sum(销量)"
            }
        }
    ],
    "elements": [
        {"type": "text", "content": "电子产品月度分析", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "monthly_summary",
            "xAxis": "日期",
            "yAxis": "total_amount",
            "title": "月度销售额"
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "table",
            "dataSource": "monthly_summary",
            "columns": ["日期", "total_amount", "total_sales"]
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("raw_data", data)
generator.save("output/pipeline_workflow.pdf")
```
