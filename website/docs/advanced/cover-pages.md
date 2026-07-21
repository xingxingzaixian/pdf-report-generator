# 封面页

创建专业的报告封面，支持背景图片、渐变和多种预设模板。

## 基本封面

```json
{
  "elements": [
    {
      "type": "cover",
      "title": "年度销售报告",
      "subtitle": "2024 年第一季度",
      "author": "财务部",
      "date": "2024-04-01"
    },
    {
      "type": "pagebreak"
    },
    {
      "type": "toc",
      "title": "目录"
    }
  ]
}
```

## 封面属性

| 属性 | 说明 |
|------|------|
| `title` | 报告标题 |
| `subtitle` | 副标题 |
| `author` | 作者/部门 |
| `date` | 日期 |
| `logo` | Logo 图片路径 |
| `background` | 背景图片路径 |
| `template` | 预设模板名称 |

## 背景图片

```json
{
  "type": "cover",
  "title": "年度报告",
  "background": "images/cover-bg.jpg",
  "logo": "images/company-logo.png"
}
```

## 预设模板

### minimal - 极简风格

```json
{
  "type": "cover",
  "template": "minimal",
  "title": "简洁报告"
}
```

### corporate - 企业风格

```json
{
  "type": "cover",
  "template": "corporate",
  "title": "企业年度报告",
  "subtitle": "2024 财年",
  "author": "战略规划部"
}
```

### gradient - 渐变风格

```json
{
  "type": "cover",
  "template": "gradient",
  "title": "数据分析报告",
  "gradientColors": ["#4472C4", "#2d4a7a"]
}
```

## 自定义封面样式

```json
{
  "type": "cover",
  "title": "自定义封面",
  "titleStyle": {
    "fontSize": 36,
    "textColor": "#FFFFFF",
    "alignment": "center"
  },
  "subtitleStyle": {
    "fontSize": 18,
    "textColor": "#CCCCCC"
  },
  "backgroundColor": "#1a1a2e"
}
```

## 完整示例

```json
{
  "metadata": {
    "title": "年度报告",
    "pageSize": "A4"
  },
  "elements": [
    {
      "type": "cover",
      "template": "corporate",
      "title": "2024 年度销售报告",
      "subtitle": "第一季度业绩分析",
      "author": "销售部",
      "date": "2024-04-01",
      "logo": "images/logo.png"
    },
    {
      "type": "pagebreak"
    },
    {
      "type": "toc",
      "title": "目录"
    },
    {
      "type": "pagebreak"
    },
    {
      "type": "text",
      "content": "报告正文...",
      "style": "body"
    }
  ]
}
```

## 下一步

- [自动目录](./table-of-contents.md) - 配合封面使用目录
- [页眉页脚](./headers-footers.md) - 添加页眉页脚
