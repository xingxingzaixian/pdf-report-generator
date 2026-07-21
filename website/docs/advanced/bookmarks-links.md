# 超链接与书签

在 PDF 中添加可点击的超链接和文档书签。

## 超链接

### 文本中的超链接

```json
{
  "type": "text",
  "content": "访问 <a href='https://example.com'>示例网站</a> 了解更多信息"
}
```

### 独立链接元素

```json
{
  "type": "link",
  "url": "https://example.com",
  "text": "点击访问",
  "style": "linkStyle"
}
```

## 书签

书签帮助读者在 PDF 阅读器中快速导航。

### 添加书签

```json
{
  "type": "bookmark",
  "title": "第一章 概述",
  "level": 1
}
```

### 书签层级

```json
[
  {"type": "bookmark", "title": "第一章", "level": 1},
  {"type": "bookmark", "title": "1.1 背景", "level": 2},
  {"type": "bookmark", "title": "1.2 目标", "level": 2},
  {"type": "bookmark", "title": "第二章", "level": 1}
]
```

## 与目录配合

目录（TOC）会自动收集标题并生成带超链接的目录项：

```json
{
  "elements": [
    {
      "type": "toc",
      "title": "目录"
    },
    {
      "type": "pagebreak"
    },
    {
      "type": "text",
      "content": "第一章 概述",
      "style": "heading1"
    }
  ]
}
```

## 内部跳转

在 PDF 中创建内部跳转链接：

```json
{
  "type": "text",
  "content": "跳转到 <a href='#section2'>第二节</a>"
},
{
  "type": "text",
  "content": "第二节内容",
  "anchor": "section2"
}
```

## 最佳实践

1. **目录自动生成** - 使用 `toc` 元素自动收集标题
2. **合理使用书签** - 为重要章节添加书签
3. **链接文本描述性** - 使用有意义的链接文本，避免"点击这里"
4. **测试跳转** - 生成后在 PDF 阅读器中测试链接

## 下一步

- [自动目录](./table-of-contents.md) - 生成可点击的目录
- [封面页](./cover-pages.md) - 创建专业的封面
