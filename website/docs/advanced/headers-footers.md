# 页眉页脚

支持在每页顶部和底部添加自定义内容，包括文本、图片和页码。

## 基本配置

在 `metadata` 中配置页眉页脚：

```json
{
  "metadata": {
    "title": "报告标题",
    "header": {
      "left": "公司名称",
      "center": "报告标题",
      "right": "机密文件"
    },
    "footer": {
      "left": "© 2024 公司",
      "center": "",
      "right": "第 {{page}} 页"
    }
  }
}
```

## 三栏布局

页眉页脚支持左、中、右三栏：

```json
{
  "header": {
    "left": "左侧内容",
    "center": "中间内容",
    "right": "右侧内容"
  }
}
```

每栏可以独立设置样式。

## 支持的变量

- `{{page}}` - 当前页码
- `{{pages}}` - 总页数
- `{{title}}` - 文档标题
- `{{date}}` - 当前日期

## 图片页眉

```json
{
  "header": {
    "left": {
      "type": "image",
      "path": "images/logo.png",
      "width": 100
    },
    "right": "报告标题"
  }
}
```

## 样式自定义

```json
{
  "header": {
    "left": "公司名称",
    "leftStyle": {
      "fontSize": 8,
      "textColor": "#999999"
    },
    "right": "第 {{page}} 页",
    "rightStyle": {
      "fontSize": 8,
      "textColor": "#999999"
    }
  }
}
```

## 完整示例

```json
{
  "metadata": {
    "title": "年度报告",
    "pageSize": "A4",
    "header": {
      "left": "ABC 公司",
      "center": "2024 年度报告",
      "right": "机密"
    },
    "footer": {
      "left": "© 2024 ABC 公司",
      "center": "",
      "right": "第 {{page}} 页 / 共 {{pages}} 页"
    }
  }
}
```

## 下一步

- [页码格式](./page-numbers.md) - 了解更多页码格式
- [封面页](./cover-pages.md) - 创建专业的封面
