# 配置结构总览

PDF 报告通过 JSON 配置文件（或字典）定义。一个完整的配置包含以下顶层字段：

```json
{
  "metadata": { ... },
  "styles": { ... },
  "dataSources": [ ... ],
  "elements": [ ... ]
}
```

## 顶层结构

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `metadata` | object | 是 | PDF 文档的元数据（标题、页面大小等） |
| `styles` | object | 否 | 样式定义，供元素引用 |
| `dataSources` | array | 否 | 数据源定义列表 |
| `elements` | array | 是 | PDF 内容元素列表 |

## 完整示例

```json
{
  "metadata": {
    "title": "销售分析报告",
    "author": "系统",
    "pageSize": "A4",
    "orientation": "portrait",
    "margin": 0.75
  },
  "styles": {
    "title": {
      "fontSize": 24,
      "textColor": "#333333",
      "alignment": "center",
      "bold": true
    },
    "tableStyle": {
      "gridColor": "#CCCCCC",
      "headerBackground": "#4472C4",
      "headerTextColor": "#FFFFFF",
      "fontSize": 9
    }
  },
  "dataSources": [
    {
      "name": "sales_data",
      "type": "csv",
      "path": "data/sales.csv"
    }
  ],
  "elements": [
    {
      "type": "text",
      "content": "{{metadata.title}}",
      "style": "title"
    },
    {
      "type": "table",
      "dataSource": "sales_data",
      "columns": ["产品", "销量", "金额"],
      "style": "tableStyle"
    }
  ]
}
```

## 配置流程

```
1. 定义 metadata ──▶ 设置文档基本信息（标题、页面大小等）
2. 定义 styles   ──▶ 创建可复用的样式定义
3. 定义 dataSources ──▶ 配置数据来源（文件、API、数据库）
4. 组织 elements  ──▶ 按顺序排列内容元素
```

## 下一步

- [元数据配置](./metadata.md) - 了解元数据的详细配置
- [样式系统](./styles.md) - 了解样式定义
- [元素系统](./elements.md) - 了解可用元素类型
- [数据源](./data-sources.md) - 了解数据源配置
