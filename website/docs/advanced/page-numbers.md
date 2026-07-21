# 页码格式

支持多种页码格式，可在页眉页脚和正文中使用。

## 支持的格式

### 阿拉伯数字（默认）

```
1, 2, 3, 4, ...
```

### 罗马数字

```
I, II, III, IV, ...
```

### 中文数字

```
一, 二, 三, 四, ...
```

## 在页脚中使用

```json
{
  "metadata": {
    "footer": {
      "right": {
        "pageNumber": true,
        "format": "arabic"
      }
    }
  }
}
```

### 罗马数字页码

```json
{
  "footer": {
    "right": {
      "pageNumber": true,
      "format": "roman"
    }
  }
}
```

### 中文页码

```json
{
  "footer": {
    "right": {
      "pageNumber": true,
      "format": "chinese"
    }
  }
}
```

## 在文本元素中使用

```json
{
  "type": "text",
  "content": "第 {{page}} 页"
}
```

## 页码样式

```json
{
  "footer": {
    "right": {
      "pageNumber": true,
      "format": "arabic",
      "style": {
        "fontSize": 10,
        "textColor": "#666666"
      }
    }
  }
}
```

## 下一步

- [自动目录](./table-of-contents.md) - 生成可点击的目录
- [超链接与书签](./bookmarks-links.md) - 添加跳转链接
