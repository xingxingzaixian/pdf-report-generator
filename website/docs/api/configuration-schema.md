# 配置 Schema

以下是 JSON 配置文件的完整结构定义。

## 顶层结构

```json
{
  "metadata": { ... },
  "styles": { ... },
  "dataSources": [ ... ],
  "pipeline": [ ... ],
  "elements": [ ... ]
}
```

## metadata

```json
{
  "title": "string",
  "author": "string",
  "pageSize": "A4 | A3 | A5 | LETTER | LEGAL",
  "orientation": "portrait | landscape",
  "margin": "number (inches)"
}
```

## styles

```json
{
  "styleName": {
    "fontSize": "number",
    "fontFamily": "string",
    "textColor": "string (#RRGGBB)",
    "backgroundColor": "string (#RRGGBB)",
    "alignment": "left | center | right | justify",
    "bold": "boolean",
    "italic": "boolean",
    "spaceBefore": "number",
    "spaceAfter": "number",
    "lineSpacing": "number",
    "gridColor": "string (表格)",
    "headerBackground": "string (表格)",
    "headerTextColor": "string (表格)",
    "padding": "number (表格)"
  }
}
```

## dataSources

```json
[
  {
    "name": "string",
    "type": "csv | excel | json | api | database",
    "path": "string (文件路径)",
    "url": "string (API 地址)",
    "method": "GET | POST",
    "headers": { ... },
    "body": "object (POST 请求体)",
    "encoding": "string",
    "sheet": "string (Excel 工作表名)",
    "dbType": "sqlite | postgresql | mysql",
    "host": "string",
    "port": "number",
    "database": "string",
    "username": "string",
    "password": "string",
    "query": "string (SQL 查询)"
  }
]
```

## pipeline

```json
[
  {
    "name": "string",
    "type": "filter | transform | aggregate",
    "source": "string (数据源名称)",
    "condition": "string (过滤条件)",
    "mappings": { ... },
    "groupBy": "string",
    "aggregations": { ... }
  }
]
```

## elements

```json
[
  {
    "type": "text | table | chart | image | spacer | pagebreak | list",
    "content": "string (text 类型)",
    "style": "string (样式名称)",
    "dataSource": "string (数据源名称)",
    "columns": ["string"],
    "columnWidths": ["number"],
    "chartType": "bar | line | pie | scatter | area",
    "xAxis": "string",
    "yAxis": "string | [string]",
    "title": "string",
    "width": "number",
    "height": "number",
    "grid": "boolean",
    "showLegend": "boolean",
    "legendPosition": "string",
    "path": "string (图片路径)",
    "alignment": "left | center | right",
    "keepAspectRatio": "boolean",
    "items": ["string"] (list 类型)
  }
]
```
