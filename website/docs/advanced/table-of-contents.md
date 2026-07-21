# 自动目录

自动生成可点击的目录（TOC），支持多级层级。

## 基本使用

在 `elements` 中添加目录元素：

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
      "content": "第一章",
      "style": "heading1"
    }
  ]
}
```

## 目录标题

```json
{
  "type": "toc",
  "title": "目录",
  "titleStyle": {
    "fontSize": 20,
    "alignment": "center"
  }
}
```

## 层级深度

控制目录显示的层级深度：

```json
{
  "type": "toc",
  "title": "目录",
  "maxDepth": 3
}
```

- `maxDepth: 1` - 只显示一级标题
- `maxDepth: 2` - 显示一、二级标题
- `maxDepth: 3` - 显示所有层级（默认）

## 标题样式映射

目录会自动收集文档中的标题。确保标题使用了正确的样式：

```json
{
  "styles": {
    "heading1": {"fontSize": 18, "bold": true},
    "heading2": {"fontSize": 14, "bold": true},
    "heading3": {"fontSize": 12, "bold": true}
  },
  "elements": [
    {
      "type": "text",
      "content": "第一章 概述",
      "style": "heading1"
    },
    {
      "type": "text",
      "content": "1.1 背景",
      "style": "heading2"
    }
  ]
}
```

## 超链接跳转

生成的目录项会自动包含超链接，点击可跳转到对应章节。

## 完整示例

```json
{
  "metadata": {
    "title": "项目报告",
    "pageSize": "A4"
  },
  "elements": [
    {
      "type": "toc",
      "title": "目录",
      "maxDepth": 2
    },
    {
      "type": "pagebreak"
    },
    {
      "type": "text",
      "content": "第一章 项目概述",
      "style": "heading1"
    },
    {
      "type": "text",
      "content": "1.1 项目背景",
      "style": "heading2"
    },
    {
      "type": "text",
      "content": "项目背景内容..."
    },
    {
      "type": "text",
      "content": "第二章 技术方案",
      "style": "heading1"
    }
  ]
}
```

## 下一步

- [封面页](./cover-pages.md) - 创建专业的封面
- [超链接与书签](./bookmarks-links.md) - 添加跳转链接
