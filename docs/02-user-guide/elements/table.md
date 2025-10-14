# 表格元素

表格元素用于展示结构化数据。

## 基本表格

```json
{
  "type": "table",
  "dataSource": "sales_data"
}
```

## 配置选项

### 指定列

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columns": ["产品", "销量", "金额"]
}
```

### 表格样式

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "style": {
    "gridColor": "#CCCCCC",
    "headerBackgroundColor": "#4472C4",
    "headerTextColor": "#FFFFFF",
    "alternateRowColor": "#F2F2F2",
    "fontSize": 9,
    "alignment": "center"
  }
}
```

## 单元格合并

```json
{
  "type": "table",
  "dataSource": "data",
  "mergeRules": [
    {
      "startRow": 0,
      "startCol": 0,
      "endRow": 0,
      "endCol": 1
    }
  ]
}
```

## 列格式化

```json
{
  "type": "table",
  "dataSource": "sales",
  "columnFormats": {
    "金额": "¥{:,.2f}",
    "增长率": "{:.1%}"
  }
}
```

# 表格自动换行功能

表格元素现在支持长文本自动换行，避免内容超出页面边界。

## 功能说明

当表格单元格中的文本过长时，可以通过配置让文本自动换行显示在多行中。

## 配置参数

### wrapColumns

指定哪些列需要自动换行（列索引从0开始）。

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columnWidths": [1.0, 2.0, 3.5],
  "wrapColumns": [2]  // 第3列（索引2）自动换行
}
```

### wrapThreshold

设置自动换行的字符长度阈值。当单元格文本超过此长度时，自动换行（默认值：50）。

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columnWidths": [1.0, 2.0, 3.5],
  "wrapThreshold": 30  // 超过30个字符自动换行
}
```

## 使用示例

### 示例1：指定列自动换行

```json
{
  "type": "table",
  "dataSource": "api_data",
  "columns": ["metric_id", "metric_name", "description"],
  "columnWidths": [1.2, 1.5, 3.8],
  "wrapColumns": [2],  // description列自动换行
  "wrapThreshold": 30
}
```

### 示例2：使用直接数据

```python
config = {
    "elements": [
        {
            "type": "table",
            "data": [
                ["ID", "名称", "描述"],
                ["1", "产品A", "这是一个很长的产品描述..."],
                ["2", "产品B", "另一个很长的描述..."]
            ],
            "columnWidths": [0.8, 1.2, 4.5],
            "wrapColumns": [2]
        }
    ]
}
```

### 示例3：多列自动换行

```json
{
  "type": "table",
  "dataSource": "data",
  "columnWidths": [1.0, 2.5, 2.5],
  "wrapColumns": [1, 2],  // 第2列和第3列都自动换行
  "wrapThreshold": 40
}
```

## 工作原理

- 当列索引在 `wrapColumns` 列表中，或
- 当单元格文本长度超过 `wrapThreshold` 时

系统会自动将文本转换为 `Paragraph` 对象，实现自动换行。

## 注意事项

1. **列宽设置**：使用自动换行时，必须设置合适的 `columnWidths`
2. **性能影响**：大量换行会增加PDF生成时间
3. **字体支持**：确保使用支持中文的字体（如 SimHei、SimSun）
4. **行高**：换行后的行高会自动调整

## 最佳实践

### 推荐配置

```json
{
  "type": "table",
  "dataSource": "data",
  "columnWidths": [1.0, 1.5, 4.0],  // 总宽度约6.5英寸（A4竖向）
  "wrapColumns": [2],  // 只对长文本列启用换行
  "wrapThreshold": 30,  // 合理的阈值
  "style": {
    "fontSize": 9,  // 适中的字体大小
    "padding": 6    // 适当的内边距
  }
}
```

### 页面宽度参考

- **A4 竖向（Portrait）**：可用宽度约 6.5 英寸
- **A4 横向（Landscape）**：可用宽度约 9.5 英寸
- **Letter 竖向**：可用宽度约 7 英寸
---

**上一页**：[文本元素](./text.md)  
**下一页**：[图表元素](./chart.md)

