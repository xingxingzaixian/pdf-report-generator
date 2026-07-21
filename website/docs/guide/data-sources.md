# 数据源

`dataSources` 数组定义数据来源，供表格和图表元素使用。

## 数据源类型

### CSV 文件

```json
{
  "name": "sales_data",
  "type": "csv",
  "path": "data/sales.csv",
  "encoding": "utf-8"
}
```

| 属性 | 说明 |
|------|------|
| `name` | 数据源名称（供元素引用） |
| `type` | 固定为 `"csv"` |
| `path` | CSV 文件路径 |
| `encoding` | 文件编码（默认 utf-8） |

### Excel 文件

```json
{
  "name": "report_data",
  "type": "excel",
  "path": "data/report.xlsx",
  "sheet": "Sheet1"
}
```

### JSON 文件

```json
{
  "name": "config_data",
  "type": "json",
  "path": "data/config.json"
}
```

### HTTP API

```json
{
  "name": "api_data",
  "type": "api",
  "url": "https://api.example.com/data",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer your-token"
  }
}
```

| 属性 | 说明 |
|------|------|
| `url` | API 地址 |
| `method` | 请求方法（GET / POST） |
| `headers` | 请求头 |
| `body` | 请求体（POST 时） |

### 数据库

```json
{
  "name": "db_data",
  "type": "database",
  "dbType": "postgresql",
  "host": "localhost",
  "port": 5432,
  "database": "mydb",
  "username": "user",
  "password": "pass",
  "query": "SELECT * FROM sales"
}
```

支持的数据库类型：`sqlite`、`postgresql`、`mysql`

## 动态添加数据源

除了在配置中静态定义，你还可以在代码中动态添加：

```python
import pandas as pd
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict=config)

# 添加 DataFrame 作为数据源
data = pd.DataFrame({"产品": ["A", "B"], "销量": [100, 200]})
generator.add_data_source("sales", data)

generator.save("output.pdf")
```

## 在元素中引用

```json
{
  "elements": [
    {
      "type": "table",
      "dataSource": "sales_data",
      "columns": ["产品", "销量"]
    },
    {
      "type": "chart",
      "chartType": "bar",
      "dataSource": "sales_data",
      "xAxis": "产品",
      "yAxis": "销量"
    }
  ]
}
```

## 下一步

- [数据管道](./pipeline.md) - 对数据进行转换和聚合
- [模板系统](./templates.md) - 了解模板的使用
