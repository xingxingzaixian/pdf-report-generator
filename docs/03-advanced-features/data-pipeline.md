# 数据管道

数据管道功能允许在报告配置中直接定义数据转换步骤，无需编写 Python 代码即可完成数据清洗、聚合和计算。

## 概述

管道定义在数据源的 `pipeline` 字段中，是一个步骤数组，按顺序执行。每个步骤包含一个 `op` 字段指定操作类型，以及操作所需的参数。

```json
{
  "dataSources": [{
    "name": "sales",
    "type": "csv",
    "path": "data/sales.csv",
    "pipeline": [
      {"op": "filter", "expr": "quantity > 100"},
      {"op": "compute", "columns": {"revenue": "quantity * price"}},
      {"op": "sort", "by": "revenue", "order": "desc"}
    ]
  }]
}
```

## 支持的操作

### filter - 数据筛选

按表达式筛选行，只保留满足条件的记录。

```json
{"op": "filter", "expr": "quantity > 100"}
```

支持的表达式语法：
- 比较运算：`>`, `<`, `>=`, `<=`, `==`, `!=`
- 逻辑运算：`and`, `or`, `not`
- 算术运算：`+`, `-`, `*`, `/`, `%`, `**`
- 字符串比较：`category == 'A'`

```json
{"op": "filter", "expr": "quantity > 100 and price < 50"}
{"op": "filter", "expr": "category == 'Electronics'"}
```

### sort - 排序

按指定列排序。

```json
{"op": "sort", "by": "revenue", "order": "desc"}
```

参数：
- `by`：排序列名（必填）
- `order`：排序方向，`asc`（升序，默认）或 `desc`（降序）

### compute - 计算列

基于现有列计算新列。

```json
{"op": "compute", "columns": {"revenue": "quantity * price"}}
```

参数：
- `columns`：字典，键为新列名，值为表达式

支持多列计算：

```json
{
  "op": "compute",
  "columns": {
    "revenue": "quantity * price",
    "profit": "revenue - cost",
    "margin": "profit / revenue * 100"
  }
}
```

### group - 分组聚合

按指定列分组并聚合。

```json
{
  "op": "group",
  "by": "category",
  "agg": {"total_revenue": "sum", "avg_price": "mean"}
}
```

参数：
- `by`：分组列名（必填）
- `agg`：聚合函数字典，支持 `sum`, `mean`, `count`, `min`, `max` 等

### select - 选择列

只保留指定的列。

```json
{"op": "select", "columns": ["product", "revenue", "margin"]}
```

### rename - 重命名列

重命名列。

```json
{"op": "rename", "columns": {"quantity": "qty", "price": "unit_price"}}
```

### concat - 合并数据源

合并多个数据源。

```json
{"op": "concat", "sources": ["sales_q1", "sales_q2"]}
```

### limit / head - 限制行数

取前 N 行。

```json
{"op": "limit", "n": 100}
```

`head` 是 `limit` 的别名，用法相同。

## 完整示例

### 销售数据处理

```json
{
  "dataSources": [{
    "name": "sales",
    "type": "csv",
    "path": "data/raw_sales.csv",
    "pipeline": [
      {"op": "filter", "expr": "quantity > 0"},
      {"op": "compute", "columns": {"revenue": "quantity * price"}},
      {"op": "group", "by": "category", "agg": {"revenue": "sum"}},
      {"op": "sort", "by": "revenue", "order": "desc"},
      {"op": "limit", "n": 10}
    ]
  }],
  "elements": [
    {
      "type": "table",
      "dataSource": "sales",
      "columns": ["category", "revenue"]
    }
  ]
}
```

### 财务报表数据

```json
{
  "dataSources": [
    {
      "name": "raw_financials",
      "type": "csv",
      "path": "data/financials.csv",
      "pipeline": [
        {"op": "filter", "expr": "amount != 0"},
        {"op": "compute", "columns": {"abs_amount": "abs(amount)"}},
        {"op": "select", "columns": ["date", "account", "abs_amount", "type"]}
      ]
    }
  ]
}
```

## 表达式安全

管道使用沙箱表达式求值器，以下操作被禁止：
- `import` 语句
- `exec`, `eval`, `compile` 函数调用
- `open` 文件操作
- 私有属性访问（以 `_` 开头的属性）

允许的操作：
- 算术运算：`+`, `-`, `*`, `/`, `%`, `**`
- 比较运算：`>`, `<`, `>=`, `<=`, `==`, `!=`
- 逻辑运算：`and`, `or`, `not`
- 内置函数：`abs`, `len`, `max`, `min`, `round`, `sum`, `int`, `float`, `str`, `bool`

## 错误处理

如果管道执行失败，系统会：
1. 打印警告信息到标准输出
2. 使用未转换的原始数据继续生成报告

要查看详细的错误信息，可以检查生成器的输出日志。

## 下一步

- **[条件渲染](./conditional-rendering.md)** - 根据数据条件显示/隐藏元素
- **[数据源详解](../02-user-guide/data-sources.md)** - 了解所有数据源类型

---

**上一页**：[表格合并](./table-merging.md)  
**下一页**：[条件渲染](./conditional-rendering.md)
