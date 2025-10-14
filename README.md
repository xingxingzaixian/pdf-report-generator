# PDF报告生成服务

一个强大、灵活的PDF报告生成系统，支持通过JSON配置文件定义报告格式，自动从多种数据源获取数据并生成专业的PDF文档。

## ✨ 特性

### 核心功能
- 📄 **JSON配置驱动** - 通过JSON文件灵活定义PDF报告结构和样式
- 🔌 **多种数据源** - 支持JSON、CSV、Excel、数据库、HTTP API等数据源
- 📊 **丰富的元素类型** - 文本、表格、图表（柱状图、折线图、饼图等）、图片
- 🎨 **自定义样式** - 完全可定制的文本和表格样式
- 🚀 **两种使用方式** - Python库直接调用 或 FastAPI Web服务
- 🔄 **模板变量支持** - 使用Jinja2模板引擎动态渲染内容
- 📈 **专业图表** - 基于Matplotlib生成高质量图表

### 高级功能 ⭐
- 📑 **页眉页脚** - 支持文本、图片、页码，左中右三栏布局，变量替换
- 📚 **自动目录** - 自动收集标题生成可点击的目录，支持多级层级
- 🎨 **封面页** - 灵活的封面设计，支持背景图片/渐变，多个预设模板
- 🔢 **多种页码格式** - 阿拉伯数字、罗马数字、中文数字
- 🔗 **超链接书签** - 目录自动添加跳转链接
- 📋 **表格合并** - 支持复杂的单元格合并
- 🈲 **中文字体** - 自动加载中文字体，完美支持中文显示

## 🚀 快速开始

### 安装

#### 方式 1: 通过 pip 安装（推荐）

```bash
# 基础安装（仅核心 PDF 生成功能）
pip install pdf-report-generator

# 安装包含 API 服务器支持
pip install pdf-report-generator[api]

# 安装所有功能
pip install pdf-report-generator[all]
```

#### 方式 2: 从源码安装（开发环境）

```bash
# 克隆项目
git clone <repository-url>
cd pdf-report

# 开发模式安装
pip install -e .

# 或安装包含 API 支持
pip install -e .[api]
```

#### 方式 3: 直接使用源码

```bash
# 克隆项目
git clone <repository-url>
cd pdf-report

# 安装依赖
pip install -r requirements.txt
```

> 📖 详细安装说明请查看 [INSTALLATION.md](INSTALLATION.md)

### 方式1: Python库使用

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 方式1: 从配置文件生成
generator = PDFReportGenerator(config_path="templates/sales_report.json")
generator.save("output.pdf")

# 方式2: 使用配置字典
config = {
    "metadata": {
        "title": "销售报告",
        "pageSize": "A4"
    },
    "elements": [
        {
            "type": "text",
            "content": "{{metadata.title}}",
            "style": "title"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("output.pdf")

# 方式3: 动态添加数据
data = pd.DataFrame({
    "产品": ["A", "B", "C"],
    "销量": [100, 200, 150]
})

generator.add_data_source("sales", data)
pdf_bytes = generator.to_bytes()  # 获取字节流
```

### 方式2: Web API服务

#### 启动服务

**使用库安装后（推荐）：**

```python
# 方式1: Python 代码启动
from pdf_generator import start_api_server

start_api_server(host="localhost", port=8080)
```

```bash
# 方式2: 命令行启动
pdf-report-api --host localhost --port 8080

# 开发模式（热重载）
pdf-report-api --reload

# 生产模式（多进程）
pdf-report-api --workers 4
```

**或使用传统方式：**

```bash
# 直接运行
python -m api.main

# 使用 uvicorn
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

#### 使用API

```python
import requests

# 生成PDF
config = {
    "metadata": {"title": "API报告"},
    "elements": [
        {"type": "text", "content": "Hello PDF!"}
    ]
}

response = requests.post(
    "http://localhost:8000/api/generate",
    json={"config": config}
)

with open("output.pdf", "wb") as f:
    f.write(response.content)
```

#### API端点

- `GET /` - 服务状态
- `POST /api/generate` - 生成PDF（JSON配置）
- `POST /api/generate/upload` - 生成PDF（文件上传）
- `POST /api/validate` - 验证配置
- `GET /api/templates` - 获取模板列表
- `GET /api/health` - 健康检查

## 📋 配置文件结构

### 完整示例

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
      "bold": true,
      "spaceBefore": 0,
      "spaceAfter": 20
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
    },
    {
      "name": "api_data",
      "type": "api",
      "url": "https://api.example.com/data"
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
    },
    {
      "type": "chart",
      "chartType": "bar",
      "dataSource": "sales_data",
      "xAxis": "产品",
      "yAxis": "销量",
      "title": "销量对比",
      "width": 6,
      "height": 4
    }
  ]
}
```

### 配置说明

#### Metadata（元数据）

| 字段 | 类型 | 说明 | 可选值 |
|------|------|------|--------|
| title | string | PDF标题 | - |
| author | string | 作者 | - |
| pageSize | string | 页面大小 | A4, A3, A5, LETTER, LEGAL |
| orientation | string | 页面方向 | portrait, landscape |
| margin | number | 页边距（英寸） | - |

#### Styles（样式）

**段落样式**
- `fontSize` - 字体大小
- `textColor` - 文本颜色（#RRGGBB）
- `alignment` - 对齐方式（left/center/right/justify）
- `bold` - 是否加粗
- `spaceBefore` - 段前间距
- `spaceAfter` - 段后间距

**表格样式**
- `gridColor` - 网格线颜色
- `headerBackground` - 表头背景色
- `headerTextColor` - 表头文字颜色
- `fontSize` - 字体大小
- `padding` - 单元格内边距

#### Data Sources（数据源）

**CSV/Excel**
```json
{
  "name": "my_data",
  "type": "csv",
  "path": "data/file.csv",
  "encoding": "utf-8"
}
```

**JSON**
```json
{
  "name": "my_data",
  "type": "json",
  "path": "data/file.json"
}
```

**API**
```json
{
  "name": "api_data",
  "type": "api",
  "url": "https://api.example.com/data",
  "method": "GET",
  "headers": {"Authorization": "Bearer token"}
}
```

**数据库**
```json
{
  "name": "db_data",
  "type": "database",
  "dbType": "postgresql",
  "host": "localhost",
  "database": "mydb",
  "username": "user",
  "password": "pass",
  "query": "SELECT * FROM sales"
}
```

#### Elements（元素）

**文本**
```json
{
  "type": "text",
  "content": "这是文本内容",
  "style": "body"
}
```

**表格**
```json
{
  "type": "table",
  "dataSource": "sales_data",
  "columns": ["列1", "列2", "列3"],
  "style": "tableStyle",
  "columnWidths": [2, 1.5, 1.5]
}
```

**图表**

支持的图表类型：`bar`（柱状图）、`line`（折线图）、`pie`（饼图）、`scatter`（散点图）、`area`（面积图）

```json
{
  "type": "chart",
  "chartType": "bar",
  "dataSource": "sales_data",
  "xAxis": "产品",
  "yAxis": "销量",
  "title": "销量对比图",
  "width": 6,
  "height": 4,
  "grid": true
}
```

**图片**
```json
{
  "type": "image",
  "path": "images/logo.png",
  "width": 200,
  "alignment": "center",
  "keepAspectRatio": true
}
```

**其他元素**
- `spacer` - 空白间隔
- `pagebreak` - 分页符
- `list` - 列表

## 📚 示例

### 示例1: 简单报告

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "简单报告"},
    "elements": [
        {
            "type": "text",
            "content": "这是一个简单的PDF报告",
            "style": "title"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("simple.pdf")
```

### 示例2: 数据表格和图表

```python
import pandas as pd
from pdf_generator import PDFReportGenerator

# 准备数据
data = pd.DataFrame({
    "产品": ["A", "B", "C"],
    "销量": [150, 230, 180],
    "金额": [45000, 69000, 54000]
})

config = {
    "metadata": {"title": "销售报告"},
    "styles": {
        "title": {"fontSize": 20, "alignment": "center"},
        "table1": {
            "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF"
        }
    },
    "elements": [
        {"type": "text", "content": "销售数据", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {"type": "table", "dataSource": "sales", "style": "table1"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销量",
            "title": "销量对比",
            "width": 6,
            "height": 4
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("sales", data)
generator.save("sales_report.pdf")
```

### 示例3: 使用配置文件

查看 `templates/` 目录下的示例配置：
- `sales_report.json` - 销售报告模板
- `financial_report.json` - 财务报告模板

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_path="templates/sales_report.json")
generator.save("output.pdf")
```

### 运行示例代码

```bash
# 独立使用示例
python examples/standalone_usage.py

# API使用示例（需要先启动API服务）
python -m api.main  # 终端1
python examples/api_usage.py  # 终端2
```

## 🏗️ 项目结构

```
pdf-report/
├── pdf_generator/           # 核心库
│   ├── core/               # PDF生成引擎
│   │   ├── generator.py    # 主生成器
│   │   ├── elements.py     # PDF元素
│   │   └── styles.py       # 样式管理
│   ├── data_sources/       # 数据源适配器
│   │   ├── base.py
│   │   ├── json_source.py
│   │   ├── csv_source.py
│   │   ├── api_source.py
│   │   └── database.py
│   ├── config/             # 配置处理
│   │   ├── parser.py
│   │   └── validator.py
│   └── utils/
│       └── chart_generator.py
├── api/                    # Web API服务
│   ├── main.py
│   ├── routes.py
│   └── models.py
├── templates/              # 配置模板
│   ├── sales_report.json
│   └── financial_report.json
├── examples/               # 使用示例
│   ├── standalone_usage.py
│   └── api_usage.py
├── data/                   # 示例数据
├── requirements.txt
└── README.md
```

## 🔧 技术栈

### 核心库
- **ReportLab** - PDF生成引擎
- **Pandas** - 数据处理
- **Matplotlib** - 图表生成
- **Jinja2** - 模板引擎
- **Pillow** - 图像处理

### Web服务
- **FastAPI** - Web框架
- **Uvicorn** - ASGI服务器
- **Pydantic** - 数据验证

### 数据源支持
- JSON/CSV/Excel文件
- HTTP API
- 数据库（SQLite/PostgreSQL/MySQL）

## 📖 API文档

启动服务后，访问以下地址查看完整API文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🛠️ 高级用法

### 自定义字体

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 注册自定义字体
pdfmetrics.registerFont(TTFont('CustomFont', 'path/to/font.ttf'))

# 在样式中使用
config = {
    "styles": {
        "custom": {
            "fontName": "CustomFont",
            "fontSize": 12
        }
    }
}
```

### 条件渲染

使用Jinja2模板语法：

```json
{
  "type": "text",
  "content": "{% if revenue > 100000 %}高收入{% else %}正常{% endif %}"
}
```

### 复杂图表

```json
{
  "type": "chart",
  "chartType": "line",
  "dataSource": "data",
  "xAxis": "month",
  "yAxis": ["revenue", "cost", "profit"],
  "title": "财务趋势",
  "width": 7,
  "height": 5,
  "grid": true,
  "showLegend": true,
  "legendPosition": "upper left"
}
```

## 📚 文档

### 快速入门
- [快速开始指南](QUICKSTART.md) - 5分钟快速上手
- [安装说明](INSTALL.md) - 详细安装步骤

### 功能文档
- [使用手册](USAGE_GUIDE.md) - 完整使用说明
- [高级功能指南](ADVANCED_FEATURES.md) - 页眉页脚、目录、封面 ⭐
- [高级功能快速参考](高级功能快速参考.md) - 快速查阅手册
- [表格合并功能](TABLE_MERGE_GUIDE.md) - 复杂表格处理
- [图片使用指南](IMAGE_GUIDE.md) - 图片插入和调整

### 配置说明
- [中文字体配置](fonts/README.md) - 中文显示支持
- [配置示例](templates/) - JSON配置模板

### 其他
- [项目总结](PROJECT_SUMMARY.md) - 项目架构和设计
- [更新日志](UPDATE_LOG.md) - 版本更新记录

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 📞 支持

如有问题，请提交Issue或联系开发团队。

---

**开始使用PDF报告生成服务，让数据可视化更简单！** 🚀

