# 安装

## 环境要求

- Python >= 3.9
- pip 或 uv 包管理器

## 安装方式

### 方式 1: 通过 pip 安装（推荐）

```bash
# 基础安装（仅核心 PDF 生成功能）
pip install pdf-report-generator

# 安装包含 API 服务器支持
pip install pdf-report-generator[api]

# 安装所有功能（包含 API 和开发工具）
pip install pdf-report-generator[all]
```

### 方式 2: 使用 uv 安装

```bash
# 基础安装
uv pip install pdf-report-generator

# 安装所有功能
uv pip install pdf-report-generator[all]
```

### 方式 3: 从源码安装（开发环境）

```bash
# 克隆项目
git clone <repository-url>
cd pdf-report-generator

# 开发模式安装
pip install -e .

# 或安装包含 API 支持
pip install -e .[api]
```

### 方式 4: 直接使用源码

```bash
# 克隆项目
git clone <repository-url>
cd pdf-report-generator

# 安装依赖
pip install -r requirements.txt
```

## 验证安装

```bash
# 检查版本
python -c "from pdf_generator import PDFReportGenerator; print('安装成功!')"
```

## 中文字体

如需在 PDF 中显示中文，请确保系统中有中文字体文件。详见 [中文字体配置](/advanced/chinese-fonts)。

## 下一步

安装完成后，可以开始创建你的 [第一个报告](./first-report.md)。
