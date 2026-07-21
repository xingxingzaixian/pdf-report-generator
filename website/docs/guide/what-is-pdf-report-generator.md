# 什么是 PDF Report Generator

PDF Report Generator 是一个基于 Python 的专业 PDF 报告生成系统。它通过 JSON 配置文件驱动报告的生成，让你无需编写复杂的排版代码即可创建高质量的 PDF 文档。

## 它解决什么问题

在企业应用中，生成 PDF 报告是一个常见需求——销售报告、财务报表、项目总结等。传统方式通常需要：

- 手动编写排版代码（ReportLab 的底层 API）
- 难以维护的模板系统
- 复杂的数据对接逻辑

PDF Report Generator 将这些问题抽象为 JSON 配置，让你只需关注"报告长什么样"和"数据从哪来"。

## 核心架构

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│  JSON 配置   │───▶│  PDF 引擎    │───▶│  PDF 文档    │
│  (报告定义)  │    │  (ReportLab) │    │  (输出)      │
└─────────────┘    └──────────────┘    └──────────────┘
       │                                      ▲
       ▼                                      │
┌─────────────┐    ┌──────────────┐           │
│  数据源     │───▶│  模板引擎     │───────────┘
│  (CSV/API等)│    │  (Jinja2)    │
└─────────────┘    └──────────────┘
```

## 两种使用方式

### 1. Python 库

直接在 Python 代码中使用，适合集成到现有系统：

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_path="report.json")
generator.save("output.pdf")
```

### 2. Web API 服务

通过 REST API 提供 PDF 生成服务，适合微服务架构：

```bash
pdf-report-api --host localhost --port 8080
```

## 下一步

- [安装](./installation.md) - 了解如何安装
- [第一个报告](./first-report.md) - 动手创建你的第一份 PDF
- [特性一览](./features.md) - 了解所有功能
