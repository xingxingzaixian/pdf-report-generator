# 数据管道

数据管道（Pipeline）允许在数据到达元素之前对其进行过滤、转换和聚合。

## 管道类型

### filter - 过滤

从数据源中筛选符合条件的行。

```json
{
  "name": "high_sales",
  "type": "filter",
  "source": "sales_data",
  "condition": "销量 > 100"
}
```

### transform - 转换

对数据进行映射和转换。

```json
{
  "name": "formatted_sales",
  "type": "transform",
  "source": "sales_data",
  "mappings": {
    "销售额": "金额 * 单价",
    "增长率": "(本期 - 上期) / 上期 * 100"
  }
}
```

### aggregate - 聚合

对数据进行分组聚合计算。

```json
{
  "name": "category_summary",
  "type": "aggregate",
  "source": "sales_data",
  "groupBy": "category",
  "aggregations": {
    "total_sales": "sum(销量)",
    "avg_price": "avg(单价)",
    "count": "count()"
  }
}
```

## 完整示例

```json
{
  "dataSources": [
    {
      "name": "raw_data",
      "type": "csv",
      "path": "data/sales.csv"
    }
  ],
  "pipeline": [
    {
      "name": "filtered",
      "type": "filter",
      "source": "raw_data",
      "condition": "销量 > 50"
    },
    {
      "name": "summary",
      "type": "aggregate",
      "source": "filtered",
      "groupBy": "产品类别",
      "aggregations": {
        "total": "sum(销量)"
      }
    }
  ],
  "elements": [
    {
      "type": "table",
      "dataSource": "summary",
      "columns": ["产品类别", "total"]
    }
  ]
}
```

## 下一步

- [模板系统](./templates.md) - 了解模板的使用
- [综合示例](/examples/comprehensive.md) - 查看完整案例
