# API 参考

PDF Report Generator 提供两种 API：

1. **Python API** - 直接在代码中使用的类和方法
2. **Web API** - 通过 HTTP 调用的 REST 接口

## 快速导航

| 文档 | 说明 |
|------|------|
| [PDFReportGenerator](./pdf-report-generator.md) | Python 类 API 参考 |
| [Web API 端点](./web-api.md) | REST API 端点说明 |
| [配置 Schema](./configuration-schema.md) | JSON 配置的完整结构定义 |

## Python API 概览

```python
from pdf_generator import PDFReportGenerator

# 创建生成器
generator = PDFReportGenerator(
    config_dict=config,       # 配置字典
    config_path="report.json", # 或配置文件路径
    font_dirs=["./fonts"]      # 字体目录
)

# 添加数据源
generator.add_data_source("name", data)

# 生成 PDF
generator.save("output.pdf")       # 保存到文件
pdf_bytes = generator.to_bytes()   # 获取字节流
```

## Web API 概览

```bash
# 启动服务
pdf-report-api --host 0.0.0.0 --port 8080

# 生成 PDF
curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"config": {...}}' \
  --output report.pdf

# 验证配置
curl -X POST http://localhost:8080/api/validate \
  -H "Content-Type: application/json" \
  -d '{"config": {...}}'
```
