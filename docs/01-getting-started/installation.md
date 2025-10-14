# 安装指南

本指南将帮助您完成PDF报告生成器的安装和环境配置。

## 系统要求

### 操作系统
- Windows 7/10/11
- macOS 10.13+
- Linux (Ubuntu 18.04+, CentOS 7+)

### Python版本
- Python 3.9 或更高版本
- 推荐使用 Python 3.9 或 3.10

### 硬件要求
- **最低配置**：2GB RAM，1GB可用磁盘空间
- **推荐配置**：4GB+ RAM，2GB+ 可用磁盘空间（用于生成大型报告）

## 安装步骤

### 方式一：从源码安装（推荐）

#### 1. 克隆项目

```bash
# 使用 Git 克隆项目
git clone https://github.com/xingxingzaixian/pdf-report-generator.git
cd pdf-report-generator
```

如果没有安装 Git，可以直接下载源码包并解压。

#### 2. 创建虚拟环境（推荐）

使用虚拟环境可以隔离项目依赖，避免版本冲突：

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

#### 3. 安装依赖

```bash
# 安装所有依赖包
pip install -r requirements.txt
```

#### 4. 安装为Python包（可选）

如果希望在任何位置导入使用：

```bash
# 开发模式安装
pip install -e .

# 或标准安装
pip install .
```

### 方式二：使用 pip 安装（如果已发布到PyPI）

```bash
pip install pdf-report-generator
```

## 依赖包说明

### 核心依赖

安装完成后，您的环境将包含以下主要库：

| 库名 | 版本 | 用途 |
|------|------|------|
| reportlab | 4.0.7 | PDF生成核心引擎 |
| pandas | 2.1.4 | 数据处理和分析 |
| matplotlib | 3.8.2 | 图表生成 |
| Pillow | 10.1.0 | 图像处理 |
| Jinja2 | 3.1.2 | 模板引擎 |

### 数据源支持

| 库名 | 版本 | 用途 |
|------|------|------|
| openpyxl | 3.1.2 | Excel文件读取 |
| requests | 2.31.0 | HTTP API调用 |
| SQLAlchemy | 2.0.23 | 数据库连接 |

### Web服务（可选）

如果需要使用Web API功能：

| 库名 | 版本 | 用途 |
|------|------|------|
| fastapi | 0.105.0 | Web框架 |
| uvicorn | 0.25.0 | ASGI服务器 |
| python-multipart | 0.0.6 | 文件上传支持 |
| pydantic | 2.5.3 | 数据验证 |

## 中文字体配置

为了正确显示中文，需要配置中文字体。

### 自动配置（推荐）

项目已包含三种中文字体，位于 `fonts/` 目录：

- **SimHei.TTF** - 黑体（默认）
- **SimSun.TTF** - 宋体
- **GB2312.TTF** - GB2312字体

这些字体会在首次导入时自动注册，无需手动配置。

### 手动配置字体

如果需要使用其他字体，可以将TTF字体文件放入 `fonts/` 目录，系统会自动扫描并注册。

#### Windows系统

Windows系统字体通常位于：
```
C:\Windows\Fonts\
```

常用中文字体：
- 微软雅黑：`msyh.ttc`
- 宋体：`simsun.ttc`
- 黑体：`simhei.ttf`

#### macOS系统

macOS系统字体位于：
```
/System/Library/Fonts/
/Library/Fonts/
```

常用中文字体：
- 苹方：`PingFang.ttc`
- 华文黑体：`STHeiti Light.ttc`

#### Linux系统

安装中文字体：

```bash
# Ubuntu/Debian
sudo apt-get install fonts-noto-cjk

# CentOS/RHEL
sudo yum install google-noto-sans-cjk-fonts
```

### 验证字体安装

运行测试脚本验证字体配置：

```bash
python test_chinese_font.py
```

如果成功，会生成一个包含中文文本的测试PDF文件。

## 验证安装

### 快速测试

运行以下Python代码验证安装：

```python
from pdf_generator import PDFReportGenerator

# 创建简单配置
config = {
    "metadata": {"title": "测试报告"},
    "elements": [
        {
            "type": "text",
            "content": "Hello, 这是一个测试PDF！",
            "style": "Normal"
        }
    ]
}

# 生成PDF
generator = PDFReportGenerator(config_dict=config)
generator.save("test.pdf")
print("✅ 安装成功！已生成 test.pdf")
```

### 运行示例

项目包含多个示例程序：

```bash
# 运行所有示例
python run_examples.py

# 运行单个示例
python examples/standalone_usage.py
```

成功运行后，会在项目根目录生成多个PDF文件。

## 数据库驱动（可选）

如果需要使用数据库数据源，需要安装相应的驱动：

### SQLite
无需额外安装，Python内置支持。

### PostgreSQL
```bash
pip install psycopg2-binary
```

### MySQL
```bash
pip install pymysql
# 或
pip install mysqlclient
```

### SQL Server
```bash
pip install pyodbc
```

## Web服务部署（可选）

如果需要部署Web API服务：

### 开发环境

```bash
# 启动开发服务器
python run_api.py

# 或使用 uvicorn
uvicorn api.main:app --reload
```

访问 `http://localhost:8000/docs` 查看API文档。

### 生产环境

```bash
# 使用 Gunicorn + Uvicorn
pip install gunicorn

# 启动服务
gunicorn api.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

详细部署说明请参考 [部署指南](./deployment.md)。

## 常见问题

### 问题1：pip安装依赖失败

**解决方案**：
```bash
# 升级pip
python -m pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题2：中文显示为方框

**原因**：PDF Report Generator 不包含字体文件，需要用户自己提供中文字体。

**解决方案**：

1. **快速解决**（推荐）：
   ```bash
   # 在项目目录创建 fonts 文件夹
   mkdir fonts
   
   # 将中文字体文件放入 fonts/ 目录
   # Windows: 从 C:\Windows\Fonts\ 复制 SimHei.ttf 和 SimSun.ttf
   # Linux: 安装字体包 sudo apt-get install fonts-wqy-microhei
   ```

2. **使用系统字体**：
   ```python
   from pdf_generator import PDFReportGenerator
   
   generator = PDFReportGenerator(
       config_dict=config,
       font_dirs=['C:\\Windows\\Fonts']  # Windows
       # font_dirs=['/usr/share/fonts']  # Linux
   )
   ```

3. **详细配置**：参考 [中文字体配置](../03-advanced-features/chinese-fonts.md)

### 问题3：matplotlib中文显示异常

**解决方案**：
```bash
# 清除matplotlib缓存
rm -rf ~/.matplotlib
# 或 Windows: 删除 C:\Users\YourName\.matplotlib
```

重新运行程序，系统会自动重新配置字体。

### 问题4：ImportError: No module named 'xxx'

**解决方案**：
- 确认已激活虚拟环境
- 重新安装依赖：`pip install -r requirements.txt`
- 检查Python版本是否符合要求

## 中文字体配置

### 重要说明

**PDF Report Generator 不包含字体文件**，需要用户自己提供中文字体。这样设计的原因：
- 字体文件较大（每个 5-20 MB），避免增加包体积
- 不同用户可能需要不同的字体
- 避免字体许可证问题
- 可以使用系统已有的字体

### 快速配置

**方式 1：使用项目目录（推荐）**

```bash
# 在项目根目录创建 fonts 文件夹
mkdir fonts

# 将中文字体文件放入该文件夹
# Windows: 从 C:\Windows\Fonts\ 复制 SimHei.ttf 和 SimSun.ttf
# Linux: 安装字体包
sudo apt-get install fonts-wqy-microhei fonts-wqy-zenhei
```

代码中无需特殊配置：

```python
from pdf_generator import PDFReportGenerator

# 会自动查找当前目录下的 fonts/
generator = PDFReportGenerator(config_dict=config)
generator.generate('output.pdf')
```

**方式 2：指定字体目录**

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[
        './fonts',                    # 当前目录
        'C:\\Windows\\Fonts',         # Windows 系统字体
        '/usr/share/fonts/chinese',   # Linux 中文字体
    ]
)
```

**方式 3：配置文件指定**

```json
{
  "metadata": {
    "title": "报告",
    "fontDirs": ["./fonts", "C:\\Windows\\Fonts"]
  }
}
```

### 验证字体配置

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict=config)
print("已注册字体：", generator.style_manager.registered_fonts)
# 输出示例：{'SimHei', 'SimSun'}
```

### 详细说明

完整的中文字体配置指南请参考：
- [中文字体配置](../03-advanced-features/chinese-fonts.md) - 详细配置说明
- [字体配置指南](../../FONT_CONFIGURATION.md) - 根目录完整指南

## 下一步

安装完成后，建议按以下顺序学习：

1. **[快速开始](./quick-start.md)** - 5分钟生成第一个PDF
2. **[创建第一个完整报告](./first-report.md)** - 分步教程
3. **[基本概念](../02-user-guide/basic-concepts.md)** - 理解核心概念
4. **[中文字体配置](../03-advanced-features/chinese-fonts.md)** - 字体配置详解

## 获取帮助

如果在安装过程中遇到问题：

- 查看 [常见问题](../07-appendix/faq.md)
- 查看 [故障排查指南](../06-development/troubleshooting.md)
- 提交 GitHub Issue

---

**上一页**：[文档首页](../README.md)  
**下一页**：[快速开始](./quick-start.md)

