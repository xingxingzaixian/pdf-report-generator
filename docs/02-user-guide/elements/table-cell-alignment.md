# 表格单元格对齐方式指南

本文档说明如何控制表格单元格内文本的对齐方式。

## 快速开始

### 方法1：通过样式设置（全局）

在样式配置中设置 `alignment` 和 `valignment`，影响整个表格：

```json
{
  "styles": {
    "my_style": {
      "alignment": "LEFT",     // 水平对齐
      "valignment": "TOP"      // 垂直对齐
    }
  },
  "elements": [
    {
      "type": "table",
      "data": [...],
      "style": "my_style"
    }
  ]
}
```

### 方法2：通过 cellAlignments（精确控制）

在表格配置中设置 `cellAlignments`，可以精确控制特定单元格：

```json
{
  "type": "table",
  "data": [...],
  "cellAlignments": [
    {
      "range": [0, 0, 5, 0],    // 第0列
      "align": "LEFT",           // 左对齐
      "valign": "MIDDLE"         // 垂直居中
    }
  ]
}
```

## 对齐选项

### 水平对齐（align）

| 值 | 说明 | 适用场景 |
|----|------|---------|
| `LEFT` | 左对齐 | 文本、名称、描述 |
| `CENTER` | 居中 | 表头、状态、类别 |
| `RIGHT` | 右对齐 | 数字、金额、数量 |

### 垂直对齐（valign）

| 值 | 说明 | 适用场景 |
|----|------|---------|
| `TOP` | 顶部对齐 | 长文本、多行内容 |
| `MIDDLE` | 居中对齐（默认） | 单行文本、数字 |
| `BOTTOM` | 底部对齐 | 特殊排版需求 |

## 范围格式说明

`range` 参数格式：`[startRow, startCol, endRow, endCol]`

- **索引从 0 开始**
- **包含起始和结束位置**

### 范围示例

```python
# 单个单元格（第1行第2列）
[1, 2, 1, 2]

# 整列（第0列，所有行）
[0, 0, 99, 0]  # 假设有100行

# 整行（第5行，所有列）
[5, 0, 5, 99]  # 假设有100列

# 矩形区域（第1-3行，第0-2列）
[1, 0, 3, 2]
```

## 实用示例

### 示例1：财务报表

```json
{
  "type": "table",
  "data": [
    ["项目", "金额", "占比"],
    ["收入", "100,000", "100%"],
    ["成本", "60,000", "60%"],
    ["利润", "40,000", "40%"]
  ],
  "cellAlignments": [
    {"range": [0, 0, 3, 0], "align": "LEFT"},     // 项目列左对齐
    {"range": [0, 1, 3, 2], "align": "RIGHT"}     // 金额和占比右对齐
  ]
}
```

### 示例2：产品列表

```json
{
  "type": "table",
  "data": [
    ["产品", "类别", "价格", "状态"],
    ["iPhone", "手机", "¥6,999", "在售"],
    ["iPad", "平板", "¥4,799", "在售"]
  ],
  "cellAlignments": [
    {"range": [0, 0, 0, 3], "align": "CENTER"},   // 表头居中
    {"range": [1, 0, 2, 0], "align": "LEFT"},     // 产品名左对齐
    {"range": [1, 1, 2, 1], "align": "CENTER"},   // 类别居中
    {"range": [1, 2, 2, 2], "align": "RIGHT"},    // 价格右对齐
    {"range": [1, 3, 2, 3], "align": "CENTER"}    // 状态居中
  ]
}
```

### 示例3：混合垂直对齐

```json
{
  "type": "table",
  "data": [
    ["标题", "这是一段很长的描述文字..."],
    ["另一标题", "短文本"]
  ],
  "rowHeights": [0.8, 0.8],  // 设置较大行高
  "cellAlignments": [
    {"range": [0, 0, 1, 0], "align": "LEFT", "valign": "TOP"},      // 标题列顶对齐
    {"range": [0, 1, 1, 1], "align": "LEFT", "valign": "MIDDLE"}    // 描述列居中
  ]
}
```

## 常见问题

### Q1: 为什么默认是垂直居中？

A: 在 `styles.py` 中，默认的表格样式设置了 `valignment: MIDDLE`。这是最常见的需求。如果需要其他对齐方式，可以通过样式或 `cellAlignments` 覆盖。

### Q2: cellAlignments 会覆盖样式设置吗？

A: 是的。`cellAlignments` 的优先级高于样式设置。处理顺序：
1. 样式中的全局对齐
2. `cellAlignments` 中的特定对齐（覆盖全局）

### Q3: 如何设置整列对齐？

A: 使用较大的 `endRow` 值：

```json
{
  "cellAlignments": [
    {"range": [0, 2, 999, 2], "align": "RIGHT"}  // 第2列右对齐
  ]
}
```

### Q4: 可以只设置水平对齐，不设置垂直对齐吗？

A: 可以。`align` 和 `valign` 都是可选的：

```json
{
  "cellAlignments": [
    {"range": [0, 0, 5, 0], "align": "LEFT"}     // 只设置水平对齐
  ]
}
```

### Q5: 如何让表头居中，数据行左对齐？

A: 使用两个 `cellAlignments` 规则：

```json
{
  "cellAlignments": [
    {"range": [0, 0, 0, 5], "align": "CENTER"},  // 表头（第0行）居中
    {"range": [1, 0, 99, 5], "align": "LEFT"}    // 数据行左对齐
  ]
}
```

## 最佳实践

### 1. 根据内容类型选择对齐方式

```
文本内容 → LEFT
数字金额 → RIGHT
状态类别 → CENTER
表头标题 → CENTER
```

### 2. 保持一致性

同一类型的列应使用相同的对齐方式。例如，所有金额列都右对齐。

### 3. 合理使用垂直对齐

- 单行内容：使用 `MIDDLE`（默认）
- 多行长文本：使用 `TOP`
- 特殊需求才用 `BOTTOM`

### 4. 优先使用样式

如果整个表格使用相同的对齐方式，在样式中设置，而不是用 `cellAlignments`：

```json
// ✅ 推荐（简洁）
{
  "styles": {
    "my_style": {
      "alignment": "LEFT",
      "valignment": "TOP"
    }
  }
}

// ❌ 不推荐（冗余）
{
  "cellAlignments": [
    {"range": [0, 0, 999, 999], "align": "LEFT", "valign": "TOP"}
  ]
}
```

### 5. 使用有意义的范围

```json
// ✅ 明确的范围
{"range": [0, 0, 5, 0], "align": "LEFT"}  // 第0列，6行数据

// ❌ 过大的范围（浪费）
{"range": [0, 0, 99999, 0], "align": "LEFT"}
```

## 演示代码

运行以下脚本查看对齐效果：

```bash
python examples/table_alignment_demo.py
```

生成4个示例PDF：
1. `table_align_01_style.pdf` - 样式对齐
2. `table_align_02_cells.pdf` - 单元格对齐
3. `table_align_03_columns.pdf` - 按列对齐
4. `table_align_04_complex.pdf` - 复杂组合

---

**相关文档**：
- [表格元素完整文档](./table.md)
- [表格样式](../styles.md)
- [表格布局参数](./table-layout-parameters.md)

