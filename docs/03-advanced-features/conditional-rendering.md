# 条件渲染与动态循环

条件渲染功能允许根据数据值决定元素是否显示，动态循环功能允许根据数据自动生成重复元素。

## 条件渲染

### 基本用法

在元素配置中添加 `condition` 字段，当表达式求值为 `true` 时显示元素，为 `false` 时隐藏元素。

```json
{
  "type": "text",
  "content": "警告：本月利润为负！",
  "style": "warning",
  "condition": "dataSources.summary.profit < 0"
}
```

### 条件表达式语法

条件表达式使用与数据管道相同的沙箱表达式求值器，支持：
- 比较运算：`>`, `<`, `>=`, `<=`, `==`, `!=`
- 逻辑运算：`and`, `or`, `not`
- 算术运算：`+`, `-`, `*`, `/`

### 引用数据源

条件表达式可以引用处理后的数据源字段，格式为 `dataSources.<数据源名>.<列名>`：

```json
{
  "condition": "dataSources.summary.total_revenue > 0"
}
```

### 引用元数据

条件表达式可以引用元数据字段：

```json
{
  "condition": "metadata.title != ''"
}
```

### 复合条件

使用 `and`/`or` 组合多个条件：

```json
{
  "condition": "dataSources.summary.revenue > 10000 and dataSources.summary.profit > 0"
}
```

### 完整示例

```json
{
  "metadata": {"title": "销售报告"},
  "dataSources": [
    {
      "name": "summary",
      "type": "inline",
      "data": {"total": [50000], "profit": [-5000]}
    }
  ],
  "elements": [
    {
      "type": "text",
      "content": "销售报告",
      "style": "title"
    },
    {
      "type": "text",
      "content": "警告：本月利润为负！",
      "style": "warning",
      "condition": "dataSources.summary.profit < 0"
    },
    {
      "type": "text",
      "content": "业绩优秀，继续保持！",
      "style": "success",
      "condition": "dataSources.summary.profit > 0"
    }
  ]
}
```

## 动态循环

### 基本用法

在元素配置中添加 `loop` 字段，为数据源中的每个唯一值生成一个元素副本。

```json
{
  "type": "heading",
  "loop": {
    "dataSource": "categories",
    "groupBy": "category"
  },
  "text": "{{current.category}} 销售数据",
  "level": 2
}
```

### loop 配置

```json
{
  "loop": {
    "dataSource": "数据源名称",
    "groupBy": "分组列名"
  }
}
```

- `dataSource`：要遍历的数据源名称（必填）
- `groupBy`：按此列的唯一值分组（必填）

### 模板变量

在循环中，使用 `{{current.列名}}` 引用当前迭代的字段值：

```json
{
  "loop": {
    "dataSource": "categories",
    "groupBy": "category"
  },
  "text": "{{current.category}} - 总计: {{current.total}}"
}
```

### 支持的字段

模板变量替换支持以下元素字段：
- `text` - 标题文本
- `content` - 文本内容
- `title` - 图表标题

### 完整示例

为每个产品类别生成独立的章节：

```json
{
  "metadata": {"title": "分类销售报告"},
  "dataSources": [
    {
      "name": "categories",
      "type": "inline",
      "data": {
        "category": ["电子产品", "服装", "食品"],
        "total": [150000, 80000, 45000]
      }
    },
    {
      "name": "category_details",
      "type": "inline",
      "data": {
        "category": ["电子产品", "电子产品", "服装", "服装", "食品"],
        "product": ["手机", "电脑", "T恤", "裤子", "零食"],
        "sales": [80000, 70000, 45000, 35000, 45000]
      }
    }
  ],
  "elements": [
    {
      "type": "heading",
      "loop": {
        "dataSource": "categories",
        "groupBy": "category"
      },
      "text": "{{current.category}} 销售数据",
      "level": 2
    },
    {
      "type": "text",
      "loop": {
        "dataSource": "categories",
        "groupBy": "category"
      },
      "content": "类别总计: {{current.total}} 元"
    }
  ]
}
```

## 组合使用

条件渲染和循环可以组合使用。循环展开后的元素会单独检查条件：

```json
{
  "type": "text",
  "loop": {
    "dataSource": "departments",
    "groupBy": "department"
  },
  "content": "{{department}} 部门超额完成任务！",
  "condition": "dataSources.departments.target_met == true"
}
```

## 错误处理

### 数据源不存在

如果 `loop` 指定的数据源不存在，系统会：
1. 打印警告信息
2. 跳过该元素，不生成任何内容

### 分组列不存在

如果 `groupBy` 指定的列不存在，系统会：
1. 打印警告信息
2. 跳过该元素

### 条件表达式无效

如果 `condition` 表达式求值失败，系统会：
1. 打印警告信息
2. 默认显示元素（fail-open 策略）

## 下一步

- **[数据管道](./data-pipeline.md)** - 在配置中定义数据转换步骤
- **[模板变量](../02-user-guide/templates.md)** - 了解更多模板语法

---

**上一页**：[数据管道](./data-pipeline.md)  
**下一页**：[中文字体](./chinese-fonts.md)
