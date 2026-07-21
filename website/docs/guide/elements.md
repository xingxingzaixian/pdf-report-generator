# 元素系统

`elements` 数组定义 PDF 中的内容，元素按顺序渲染。

## 可用元素类型

### text - 文本

```json
{
  "type": "text",
  "content": "这是文本内容",
  "style": "title"
}
```

支持 Jinja2 模板变量：

```json
{
  "type": "text",
  "content": "报告日期: {{metadata.title}}",
  "style": "body"
}
```

### table - 表格

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columns": ["产品", "销量", "金额"],
  "style": "tableStyle",
  "columnWidths": [2, 1.5, 1.5]
}
```

| 属性 | 说明 |
|------|------|
| `dataSource` | 数据源名称 |
| `columns` | 显示的列名列表 |
| `style` | 引用的表格样式 |
| `columnWidths` | 列宽比例 |
| `header` | 是否显示表头（默认 true） |

### chart - 图表

```json
{
  "type": "chart",
  "chartType": "bar",
  "dataSource": "sales_data",
  "xAxis": "产品",
  "yAxis": "销量",
  "title": "销量对比",
  "width": 6,
  "height": 4
}
```

支持的 `chartType`：`bar`、`line`、`pie`、`scatter`、`area`

| 属性 | 说明 |
|------|------|
| `chartType` | 图表类型 |
| `dataSource` | 数据源名称 |
| `xAxis` | X 轴字段 |
| `yAxis` | Y 轴字段（可为数组） |
| `title` | 图表标题 |
| `width` | 宽度（英寸） |
| `height` | 高度（英寸） |
| `grid` | 是否显示网格 |
| `showLegend` | 是否显示图例 |

### image - 图片

```json
{
  "type": "image",
  "path": "images/logo.png",
  "width": 200,
  "alignment": "center",
  "keepAspectRatio": true
}
```

### spacer - 空白间隔

```json
{
  "type": "spacer",
  "height": 0.5
}
```

### pagebreak - 分页符

```json
{
  "type": "pagebreak"
}
```

### list - 列表

```json
{
  "type": "list",
  "items": ["项目一", "项目二", "项目三"],
  "style": "body"
}
```

## 元素组合示例

```json
{
  "elements": [
    {"type": "text", "content": "销售报告", "style": "title"},
    {"type": "spacer", "height": 0.5},
    {"type": "table", "dataSource": "sales", "style": "table1"},
    {"type": "spacer", "height": 0.5},
    {"type": "chart", "chartType": "bar", "dataSource": "sales", "xAxis": "产品", "yAxis": "销量"},
    {"type": "pagebreak"},
    {"type": "image", "path": "images/chart.png", "width": 400}
  ]
}
```

## 下一步

- [数据源](./data-sources.md) - 了解如何配置数据源
- [高级功能](/advanced/headers-footers) - 页眉页脚、目录等高级功能
