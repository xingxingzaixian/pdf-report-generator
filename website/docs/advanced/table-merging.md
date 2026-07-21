# 表格合并

支持复杂的单元格合并，创建更灵活的表格布局。

## 基本合并

### 横向合并（合并列）

```json
{
  "type": "table",
  "dataSource": "data",
  "columns": ["项目", "Q1", "Q2", "Q3", "Q4", "合计"],
  "mergeCells": [
    {"row": 0, "col": 0, "rowSpan": 1, "colSpan": 2}
  ]
}
```

### 纵向合并（合并行）

```json
{
  "type": "table",
  "dataSource": "data",
  "mergeCells": [
    {"row": 0, "col": 0, "rowSpan": 3, "colSpan": 1}
  ]
}
```

## 合并规则

| 属性 | 说明 |
|------|------|
| `row` | 起始行索引（0 开始） |
| `col` | 起始列索引（0 开始） |
| `rowSpan` | 跨越的行数 |
| `colSpan` | 跨越的列数 |

## 复杂合并示例

```json
{
  "type": "table",
  "dataSource": "sales",
  "columns": ["区域", "产品", "Q1", "Q2", "Q3", "Q4", "年度合计"],
  "mergeCells": [
    {"row": 0, "col": 0, "rowSpan": 2, "colSpan": 1},
    {"row": 2, "col": 0, "rowSpan": 2, "colSpan": 1},
    {"row": 0, "col": 6, "rowSpan": 4, "colSpan": 1}
  ],
  "style": "mergedTable"
}
```

## 样式配置

为合并单元格设置统一样式：

```json
{
  "styles": {
    "mergedTable": {
      "headerBackground": "#4472C4",
      "headerTextColor": "#FFFFFF",
      "mergeCellBackground": "#E8F0FE",
      "mergeCellTextColor": "#333333",
      "mergeCellBold": true
    }
  }
}
```

## 最佳实践

1. **合理规划合并区域** - 合并前先画出表格草图
2. **保持数据一致性** - 合并单元格只保留一个值
3. **注意对齐** - 合并后的内容默认居中对齐
4. **测试输出** - 复杂合并建议先测试再正式使用

## 下一步

- [图片处理](./images.md) - 在表格中插入图片
- [中文字体](./chinese-fonts.md) - 确保中文正确显示
