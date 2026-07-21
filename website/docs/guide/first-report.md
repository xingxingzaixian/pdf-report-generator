# 第一个报告

让我们用 3 分钟创建你的第一份 PDF 报告。

## 最简示例

创建一个 Python 文件 `hello.py`：

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "我的第一份报告"
    },
    "elements": [
        {
            "type": "text",
            "content": "Hello PDF Report Generator!",
            "style": "title"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("hello.pdf")
print("报告已生成: hello.pdf")
```

运行：

```bash
python hello.py
```

你会得到一份包含标题的 PDF 文件。

## 添加表格

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 准备数据
data = pd.DataFrame({
    "产品": ["产品A", "产品B", "产品C"],
    "销量": [150, 230, 180],
    "金额": [45000, 69000, 54000]
})

config = {
    "metadata": {"title": "销售报告"},
    "elements": [
        {"type": "text", "content": "销售数据", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {"type": "table", "dataSource": "sales", "style": "table1"}
    ],
    "styles": {
        "title": {"fontSize": 20, "alignment": "center"},
        "table1": {
            "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF"
        }
    }
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)
generator.save("sales_report.pdf")
```

## 使用配置文件

你也可以将配置写在 JSON 文件中。

创建 `my_report.json`：

```json
{
  "metadata": {
    "title": "配置文件报告",
    "pageSize": "A4"
  },
  "elements": [
    {
      "type": "text",
      "content": "通过 JSON 配置文件生成的报告",
      "style": "title"
    },
    {
      "type": "spacer",
      "height": 1
    },
    {
      "type": "text",
      "content": "这种方式适合需要频繁复用的报告模板。",
      "style": "body"
    }
  ],
  "styles": {
    "title": {
      "fontSize": 24,
      "alignment": "center",
      "textColor": "#333333"
    },
    "body": {
      "fontSize": 12,
      "textColor": "#666666"
    }
  }
}
```

使用配置文件生成：

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_path="my_report.json")
generator.save("from_config.pdf")
```

## 运行示例代码

项目提供了丰富的示例：

```bash
# 运行所有示例
cd examples
bash run_all.sh

# 运行单个示例
python 01_hello_pdf.py
```

## 下一步

- [Python 库使用](./usage-python.md) - 深入了解库的使用方式
- [Web API 使用](./usage-api.md) - 通过 API 生成 PDF
- [配置结构总览](./configuration-overview.md) - 了解配置的完整结构
