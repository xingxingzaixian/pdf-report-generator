# 样式系统

`styles` 字段定义可复用的样式，供元素通过 `style` 属性引用。

## 样式定义

```json
{
  "styles": {
    "myStyle": {
      // 样式属性
    }
  }
}
```

## 段落样式

| 属性 | 类型 | 说明 |
|------|------|------|
| `fontSize` | number | 字体大小 |
| `textColor` | string | 文本颜色（#RRGGBB） |
| `alignment` | string | 对齐方式：`left` / `center` / `right` / `justify` |
| `bold` | boolean | 是否加粗 |
| `italic` | boolean | 是否斜体 |
| `fontName` | string | 字体名称 |
| `spaceBefore` | number | 段前间距 |
| `spaceAfter` | number | 段后间距 |

### 示例

```json
{
  "styles": {
    "title": {
      "fontSize": 24,
      "textColor": "#333333",
      "alignment": "center",
      "bold": true,
      "spaceBefore": 0,
      "spaceAfter": 20
    },
    "subtitle": {
      "fontSize": 16,
      "textColor": "#666666",
      "alignment": "center",
      "spaceAfter": 10
    },
    "body": {
      "fontSize": 12,
      "textColor": "#333333",
      "spaceAfter": 6
    }
  }
}
```

## 表格样式

| 属性 | 类型 | 说明 |
|------|------|------|
| `gridColor` | string | 网格线颜色 |
| `headerBackground` | string | 表头背景色 |
| `headerTextColor` | string | 表头文字颜色 |
| `fontSize` | number | 字体大小 |
| `padding` | number | 单元格内边距 |

### 示例

```json
{
  "styles": {
    "table1": {
      "headerBackground": "#4472C4",
      "headerTextColor": "#FFFFFF",
      "gridColor": "#CCCCCC",
      "fontSize": 9,
      "padding": 6
    }
  }
}
```

## 在元素中引用样式

```json
{
  "elements": [
    {
      "type": "text",
      "content": "使用 title 样式",
      "style": "title"
    },
    {
      "type": "table",
      "dataSource": "data",
      "style": "table1"
    }
  ]
}
```

## 下一步

- [元素系统](./elements.md) - 了解可用元素类型
- [中文字体](/advanced/chinese-fonts.md) - 配置中文字体
