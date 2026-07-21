# PDFReportGenerator

`PDFReportGenerator` 是核心类，用于从配置生成 PDF 文档。

## 导入

```python
from pdf_generator import PDFReportGenerator
```

## 构造函数

```python
PDFReportGenerator(
    config_dict=None,    # 配置字典
    config_path=None,    # 配置文件路径
    font_dirs=None       # 字体目录列表
)
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `config_dict` | dict | 二选一 | 配置字典 |
| `config_path` | str | 二选一 | JSON 配置文件路径 |
| `font_dirs` | list[str] | 否 | 中文字体搜索目录 |

## 方法

### add_data_source(name, data)

动态添加数据源。

```python
import pandas as pd

generator = PDFReportGenerator(config_dict=config)

# 添加 DataFrame 作为数据源
data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
generator.add_data_source("my_data", data)
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `name` | str | 数据源名称 |
| `data` | DataFrame/dict/list | 数据内容 |

### save(output_path)

生成 PDF 并保存到文件。

```python
generator.save("output.pdf")
```

| 参数 | 类型 | 说明 |
|------|------|------|
| `output_path` | str | 输出文件路径 |

### to_bytes()

生成 PDF 并返回字节流。

```python
pdf_bytes = generator.to_bytes()
```

**返回值**: `bytes` - PDF 文件内容

### generate(output_path)

`save` 的别名方法。

```python
generator.generate("output.pdf")
```

## 完整示例

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 配置
config = {
    "metadata": {"title": "销售报告", "pageSize": "A4"},
    "styles": {
        "title": {"fontSize": 24, "alignment": "center"},
        "table1": {"headerBackground": "#4472C4", "headerTextColor": "#FFFFFF"}
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {"type": "table", "dataSource": "sales", "style": "table1"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销量",
            "title": "销量对比"
        }
    ]
}

# 创建生成器
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=["./fonts"]
)

# 添加数据
data = pd.DataFrame({
    "产品": ["A", "B", "C"],
    "销量": [150, 230, 180]
})
generator.add_data_source("sales", data)

# 保存
generator.save("sales_report.pdf")
```
