# 模板系统

PDF Report Generator 提供了多种模板机制，帮助你快速创建报告。

## 内置模板

项目提供了多个预设模板：

- `templates/sales_report.json` - 销售报告模板
- `templates/financial_report.json` - 财务报告模板
- `templates/pipeline_demo.json` - 数据管道演示模板

### 使用内置模板

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_path="templates/sales_report.json")
generator.save("output.pdf")
```

## Jinja2 模板变量

配置内容支持 Jinja2 模板语法，可以在 JSON 中使用变量和表达式。

### 变量替换

```json
{
  "type": "text",
  "content": "报告标题: {{metadata.title}}"
}
```

### 条件渲染

```json
{
  "type": "text",
  "content": "{% if revenue > 100000 %}高收入{% else %}正常{% endif %}"
}
```

### 循环

```json
{
  "type": "list",
  "items": [
    "{% for item in products %}{{ item.name }} - {{ item.price }}{% endfor %}"
  ]
}
```

## API 获取模板列表

启动 API 服务后，可以获取可用模板列表：

```bash
curl http://localhost:8080/api/templates
```

## 创建自定义模板

1. 复制一个现有模板
2. 修改配置内容
3. 保存为 `.json` 文件
4. 在代码中引用

```python
generator = PDFReportGenerator(config_path="my_templates/custom_report.json")
generator.save("output.pdf")
```

## 下一步

- [条件渲染](/advanced/conditional-rendering.md) - 深入了解条件渲染
- [部署](./deployment.md) - 了解如何部署服务
