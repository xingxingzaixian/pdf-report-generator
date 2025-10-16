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

### 列宽和行高

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columnWidths": [1.5, 2.0, 2.5],  // 单位：英寸
  "rowHeights": [0.3, 0.4, 0.4]     // 单位：英寸（可选）
}
```

## 单元格合并

使用 `mergedCells` 参数合并单元格，格式为 `[startRow, startCol, endRow, endCol]`。

**注意**：行列索引从 0 开始，且必须在表格范围内。

```json
{
  "type": "table",
  "data": [
    ["标题1", "标题2", "标题3", "标题4"],
    ["A", "B", "C", "D"],
    ["E", "F", "G", "H"]
  ],
  "mergedCells": [
    [0, 0, 0, 1]  // 合并第0行的第0-1列（标题1和标题2）
  ]
}
```

### 合并单元格示例

```json
{
  "type": "table",
  "data": [
    ["姓名", "成绩", "", ""],
    ["", "语文", "数学", "英语"],
    ["张三", "90", "85", "88"],
    ["李四", "92", "88", "90"]
  ],
  "mergedCells": [
    [0, 0, 1, 0],  // 合并"姓名"列的前两行
    [0, 1, 0, 3]   // 合并"成绩"横跨3列
  ]
}
```

## 表格布局参数

### 跨页显示设置

当表格内容较多需要跨页显示时，可以控制哪些行/列在每页重复显示。

#### repeatRows

指定跨页时在每页顶部重复显示的行数。默认值为 `1`（重复表头）。

```json
{
  "type": "table",
  "dataSource": "large_dataset",
  "repeatRows": 1  // 每页都显示表头
}
```

**使用场景**：
- `repeatRows: 0` - 不重复任何行（表头只在第一页）
- `repeatRows: 1` - 重复第一行（通常是表头）
- `repeatRows: 2` - 重复前两行（例如：主标题 + 副标题）

#### repeatCols

指定跨页时在每页左侧重复显示的列数。默认值为 `0`。

```json
{
  "type": "table",
  "dataSource": "wide_table",
  "repeatCols": 1,  // 每页都显示第一列（如：姓名列）
  "columnWidths": [1.0, 2.0, 2.0, 2.0]
}
```

### 表格分割方式

#### splitByRow

控制表格跨页时如何分割。默认值为 `true`。

```json
{
  "type": "table",
  "dataSource": "data",
  "splitByRow": true  // 按行分割（推荐）
}
```

- `true`：按行分割，一行不会被拆分到两页
- `false`：允许在行内分割（较少使用）

### 表格对齐

#### hAlign - 水平对齐

控制表格在页面中的水平位置。可选值：`LEFT`、`CENTER`、`RIGHT`。默认为 `LEFT`。

```json
{
  "type": "table",
  "dataSource": "data",
  "hAlign": "CENTER",  // 表格居中显示
  "columnWidths": [1.5, 2.0, 2.0]
}
```

#### vAlign - 垂直对齐

控制表格在可用空间中的垂直位置。可选值：`TOP`、`MIDDLE`、`BOTTOM`。默认为 `TOP`。

```json
{
  "type": "table",
  "dataSource": "data",
  "vAlign": "MIDDLE"  // 在可用空间中垂直居中
}
```

### 表格间距

#### spaceBefore / spaceAfter

设置表格前后的空白间距（单位：英寸）。

```json
{
  "type": "table",
  "dataSource": "data",
  "spaceBefore": 0.3,  // 表格前留0.3英寸空白
  "spaceAfter": 0.5    // 表格后留0.5英寸空白
}
```

### 综合示例

```json
{
  "type": "table",
  "dataSource": "employee_data",
  "columns": ["姓名", "部门", "职位", "薪资"],
  "columnWidths": [1.2, 1.5, 1.8, 1.5],
  "repeatRows": 1,      // 每页重复表头
  "repeatCols": 1,      // 每页重复姓名列
  "splitByRow": true,   // 按行分割
  "hAlign": "CENTER",   // 表格居中
  "spaceBefore": 0.2,
  "spaceAfter": 0.3,
  "style": "default"
}
```

---

# 表格自动换行功能

表格元素支持长文本自动换行，避免内容超出页面边界。

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

## 单元格对齐方式

### 通过样式设置全局对齐

在样式中设置 `alignment` 和 `valignment` 可以控制整个表格所有单元格的对齐方式：

```json
{
  "styles": {
    "my_table_style": {
      "gridColor": "#CCCCCC",
      "headerBackground": "#4472C4",
      "headerTextColor": "#FFFFFF",
      "fontSize": 9,
      "alignment": "LEFT",      // 水平对齐：LEFT/CENTER/RIGHT
      "valignment": "TOP"       // 垂直对齐：TOP/MIDDLE/BOTTOM
    }
  },
  "elements": [
    {
      "type": "table",
      "data": [...],
      "style": "my_table_style"
    }
  ]
}
```

**可选值**：
- **alignment**（水平对齐）：`LEFT`（左对齐）、`CENTER`（居中）、`RIGHT`（右对齐）
- **valignment**（垂直对齐）：`TOP`（顶部）、`MIDDLE`（居中）、`BOTTOM`（底部）

**默认值**：
- `alignment`: `LEFT`
- `valignment`: `MIDDLE`

### 设置特定单元格/列/行的对齐

使用 `cellAlignments` 参数可以精确控制特定单元格、列或行的对齐方式：

```json
{
  "type": "table",
  "data": [
    ["姓名", "年龄", "薪资"],
    ["张三", "28", "¥8,000"],
    ["李四", "32", "¥12,000"]
  ],
  "cellAlignments": [
    // 姓名列左对齐
    {"range": [0, 0, 2, 0], "align": "LEFT"},
    // 年龄列居中对齐
    {"range": [0, 1, 2, 1], "align": "CENTER"},
    // 薪资列右对齐
    {"range": [0, 2, 2, 2], "align": "RIGHT"}
  ]
}
```

**cellAlignments 格式**：
```json
{
  "range": [startRow, startCol, endRow, endCol],  // 单元格范围
  "align": "LEFT/CENTER/RIGHT",                   // 水平对齐（可选）
  "valign": "TOP/MIDDLE/BOTTOM"                   // 垂直对齐（可选）
}
```

**范围说明**：
- 索引从 0 开始
- `[0, 0, 2, 0]` 表示第 0-2 行的第 0 列（整列）
- `[1, 0, 1, 2]` 表示第 1 行的第 0-2 列（整行）
- `[1, 1, 1, 1]` 表示第 1 行第 1 列（单个单元格）

### 对齐方式使用场景

| 场景 | 推荐对齐方式 | 示例 |
|------|-------------|------|
| 文本内容（名称、描述） | 左对齐（LEFT） | 姓名、产品名称 |
| 数字、金额 | 右对齐（RIGHT） | 价格、数量、总计 |
| 状态、类别 | 居中（CENTER） | 等级、状态标识 |
| 表头 | 居中（CENTER） | 所有列标题 |
| 长文本 | 左对齐 + 顶部对齐（LEFT + TOP） | 描述、备注 |

### 完整对齐示例

```json
{
  "type": "table",
  "data": [
    ["产品名称", "类别", "单价", "库存", "状态"],
    ["MacBook Pro", "电脑", "¥18,999", "25", "在售"],
    ["iPad Air", "平板", "¥4,799", "50", "在售"],
    ["iPhone 15", "手机", "¥6,999", "100", "热销"]
  ],
  "columnWidths": [2.0, 1.2, 1.5, 1.0, 1.0],
  "cellAlignments": [
    // 表头居中
    {"range": [0, 0, 0, 4], "align": "CENTER", "valign": "MIDDLE"},
    // 产品名称左对齐
    {"range": [1, 0, 3, 0], "align": "LEFT"},
    // 类别居中
    {"range": [1, 1, 3, 1], "align": "CENTER"},
    // 单价和库存右对齐
    {"range": [1, 2, 3, 3], "align": "RIGHT"},
    // 状态居中
    {"range": [1, 4, 3, 4], "align": "CENTER"}
  ]
}
```

---

## 完整配置参数参考

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `type` | string | - | **必填**，值为 `"table"` |
| `dataSource` | string | - | 数据源名称（与 `data` 二选一） |
| `data` | array | - | 直接提供的表格数据（与 `dataSource` 二选一） |
| `columns` | array | 所有列 | 要显示的列名列表 |
| `headers` | array | 列名 | 自定义表头 |
| `style` | string | `"default"` | 表格样式名称 |
| `columnWidths` | array | 自动 | 列宽列表（英寸） |
| `rowHeights` | array | 自动 | 行高列表（英寸） |
| `mergedCells` | array | `[]` | 合并单元格配置 `[[startRow, startCol, endRow, endCol], ...]` |
| `wrapColumns` | array | `[]` | 需要自动换行的列索引列表 |
| `wrapThreshold` | number | `50` | 自动换行的字符长度阈值 |
| `repeatRows` | number | `1` | 跨页时重复显示的行数 |
| `repeatCols` | number | `0` | 跨页时重复显示的列数 |
| `splitByRow` | boolean | `true` | 是否按行分割表格 |
| `hAlign` | string | `"LEFT"` | 表格水平对齐（`LEFT`/`CENTER`/`RIGHT`） |
| `vAlign` | string | `"TOP"` | 表格垂直对齐（`TOP`/`MIDDLE`/`BOTTOM`） |
| `spaceBefore` | number | - | 表格前的空白高度（英寸） |
| `spaceAfter` | number | - | 表格后的空白高度（英寸） |
| `cellAlignments` | array | `[]` | 单元格对齐设置 `[{"range": [r1,c1,r2,c2], "align": "...", "valign": "..."}]` |

### 完整示例

```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columns": ["产品", "销量", "金额", "描述"],
  "columnWidths": [1.5, 1.2, 1.3, 3.0],
  "rowHeights": [0.35],
  "wrapColumns": [3],
  "wrapThreshold": 40,
  "repeatRows": 1,
  "repeatCols": 0,
  "splitByRow": true,
  "hAlign": "CENTER",
  "vAlign": "TOP",
  "spaceBefore": 0.2,
  "spaceAfter": 0.3,
  "style": "default",
  "mergedCells": []
}
```

---

**上一页**：[文本元素](./text.md)  
**下一页**：[图表元素](./chart.md)

