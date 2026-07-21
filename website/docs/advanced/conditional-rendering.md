# 条件渲染

使用 Jinja2 模板语法实现条件渲染，根据数据动态显示内容。

## 基本语法

### if 语句

```json
{
  "type": "text",
  "content": "{% if revenue > 100000 %}高收入{% else %}正常{% endif %}"
}
```

### if-elif-else

```json
{
  "type": "text",
  "content": "{% if score >= 90 %}优秀{% elif score >= 60 %}合格{% else %}不合格{% endif %}"
}
```

### 条件显示元素

```json
{
  "type": "chart",
  "chartType": "bar",
  "dataSource": "data",
  "xAxis": "month",
  "yAxis": "revenue",
  "visible": "{% if showChart %}true{% else %}false{% endif %}"
}
```

## 循环渲染

### 遍历列表

```json
{
  "type": "list",
  "items": [
    "{% for item in products %}{{ item.name }}: {{ item.price }}{% endfor %}"
  ]
}
```

### 表格动态行

```json
{
  "type": "table",
  "dataSource": "dynamic_data",
  "columns": ["名称", "状态"],
  "rowStyles": {
    "warning": "{% if row.status == '异常' %}warningRow{% endif %}"
  }
}
```

## 变量使用

### 文本中嵌入变量

```json
{
  "type": "text",
  "content": "报告周期: {{period}} | 生成时间: {{generatedAt}}"
}
```

### 条件样式

```json
{
  "type": "text",
  "content": "当前状态",
  "style": "{% if status == '正常' %}greenStyle{% else %}redStyle{% endif %}"
}
```

## 完整示例

```json
{
  "metadata": {"title": "条件渲染报告"},
  "dataSources": [
    {
      "name": "metrics",
      "type": "json",
      "path": "data/metrics.json"
    }
  ],
  "elements": [
    {
      "type": "text",
      "content": "{% if metrics.revenue > 1000000 %}营收超标{% else %}营收未达标{% endif %}",
      "style": "title"
    },
    {
      "type": "table",
      "dataSource": "metrics",
      "visible": "{% if metrics.showDetail %}true{% else %}false{% endif %}"
    },
    {
      "type": "chart",
      "chartType": "line",
      "dataSource": "metrics",
      "xAxis": "month",
      "yAxis": "revenue",
      "title": "月度营收趋势",
      "visible": "{% if metrics.showChart %}true{% else %}false{% endif %}"
    }
  ]
}
```

## 下一步

- [超链接与书签](./bookmarks-links.md) - 添加跳转链接
- [模板系统](/guide/templates.md) - 了解模板的使用
