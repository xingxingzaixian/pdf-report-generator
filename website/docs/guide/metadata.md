# 元数据配置

`metadata` 字段定义 PDF 文档的基本属性。

## 字段说明

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `title` | string | - | PDF 文档标题 |
| `author` | string | - | 文档作者 |
| `pageSize` | string | `"A4"` | 页面大小 |
| `orientation` | string | `"portrait"` | 页面方向 |
| `margin` | number | `0.75` | 页边距（英寸） |

## 页面大小

支持的页面大小：

- `A3` (297 x 420 mm)
- `A4` (210 x 297 mm)
- `A5` (148 x 210 mm)
- `LETTER` (8.5 x 11 英寸)
- `LEGAL` (8.5 x 14 英寸)

## 页面方向

- `portrait` - 纵向（默认）
- `landscape` - 横向

## 示例

```json
{
  "metadata": {
    "title": "年度销售报告",
    "author": "财务部",
    "pageSize": "A4",
    "orientation": "portrait",
    "margin": 0.75
  }
}
```

### 横向 A3 报告

```json
{
  "metadata": {
    "title": "大型图表报告",
    "pageSize": "A3",
    "orientation": "landscape",
    "margin": 0.5
  }
}
```
