# 综合示例

## 销售报告

一个完整的销售报告示例，包含封面、目录、图表和表格：

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 销售数据
sales_data = pd.DataFrame({
    "产品": ["产品A", "产品B", "产品C", "产品D", "产品E"],
    "Q1": [150, 230, 180, 310, 260],
    "Q2": [180, 250, 200, 290, 280],
    "Q3": [200, 280, 220, 320, 300],
    "Q4": [220, 300, 240, 350, 320],
    "年度合计": [750, 1060, 840, 1270, 1160]
})

config = {
    "metadata": {
        "title": "年度销售报告",
        "author": "销售部",
        "pageSize": "A4",
        "header": {
            "left": "ABC 公司",
            "center": "2024 年度销售报告",
            "right": "机密"
        },
        "footer": {
            "left": "© 2024 ABC 公司",
            "right": "第 {{page}} 页 / 共 {{pages}} 页"
        }
    },
    "styles": {
        "title": {"fontSize": 24, "alignment": "center", "bold": true},
        "heading1": {"fontSize": 18, "bold": true, "spaceBefore": 20},
        "heading2": {"fontSize": 14, "bold": true, "spaceBefore": 15},
        "table1": {
            "headerBackground": "#4472C4",
            "headerTextColor": "#FFFFFF",
            "fontSize": 9
        }
    },
    "elements": [
        {
            "type": "cover",
            "template": "corporate",
            "title": "2024 年度销售报告",
            "subtitle": "全年业绩回顾与分析",
            "author": "销售部",
            "date": "2024-12-31"
        },
        {"type": "pagebreak"},
        {"type": "toc", "title": "目录"},
        {"type": "pagebreak"},
        {
            "type": "text",
            "content": "一、年度销售概况",
            "style": "heading1"
        },
        {
            "type": "text",
            "content": "本年度公司销售业绩稳步增长，全年销售额达到 5080 万元，同比增长 15.3%。"
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "年度合计",
            "title": "各产品年度销量",
            "width": 6,
            "height": 4
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "text",
            "content": "二、季度销售明细",
            "style": "heading1"
        },
        {
            "type": "table",
            "dataSource": "sales",
            "style": "table1"
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "line",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": ["Q1", "Q2", "Q3", "Q4"],
            "title": "各产品季度走势",
            "width": 7,
            "height": 4,
            "showLegend": true
        }
    ]
}

generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=["./fonts"]
)
generator.add_data_source("sales", sales_data)
generator.save("output/comprehensive_sales.pdf")
```

## 财务报告

```python
from pdf_generator import PDFReportGenerator
import pandas as pd

# 财务数据
revenue_data = pd.DataFrame({
    "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
    "收入": [120, 135, 128, 142, 156, 168],
    "成本": [80, 85, 82, 88, 92, 95],
    "利润": [40, 50, 46, 54, 64, 73]
})

config = {
    "metadata": {
        "title": "财务分析报告",
        "pageSize": "A4",
        "header": {
            "left": "财务部",
            "right": "机密"
        }
    },
    "elements": [
        {"type": "text", "content": "上半年财务分析", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "finance",
            "xAxis": "月份",
            "yAxis": ["收入", "成本", "利润"],
            "title": "月度财务数据",
            "width": 7,
            "height": 4,
            "showLegend": true
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "pie",
            "dataSource": "finance",
            "xAxis": "月份",
            "yAxis": "利润",
            "title": "利润分布"
        }
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("finance", revenue_data)
generator.save("output/financial_report.pdf")
```

## 项目报告

```python
from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "项目进展报告",
        "pageSize": "A4"
    },
    "elements": [
        {"type": "text", "content": "项目进展报告", "style": "title"},
        {"type": "spacer", "height": 0.5},
        {
            "type": "text",
            "content": "一、项目概况"
        },
        {"type": "spacer", "height": 0.3},
        {
            "type": "table",
            "dataSource": "project_info"
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "text",
            "content": "二、里程碑进度"
        },
        {"type": "spacer", "height": 0.3},
        {
            "type": "table",
            "dataSource": "milestones",
            "columns": ["里程碑", "计划日期", "实际日期", "状态"]
        },
        {"type": "spacer", "height": 0.5},
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "milestones",
            "xAxis": "里程碑",
            "yAxis": "完成度",
            "title": "进度完成情况"
        }
    ]
}

project_info = [
    {"项目名称": "PDF 报告系统", "项目经理": "张三", "状态": "进行中"},
    {"项目名称": "PDF 报告系统", "开始日期": "2024-01-01", "预计完成": "2024-06-30"}
]

milestones = [
    {"里程碑": "需求分析", "计划日期": "2024-01-15", "实际日期": "2024-01-15", "状态": "已完成", "完成度": 100},
    {"里程碑": "系统设计", "计划日期": "2024-02-28", "实际日期": "2024-03-05", "状态": "已完成", "完成度": 100},
    {"里程碑": "核心开发", "计划日期": "2024-04-30", "实际日期": "-", "状态": "进行中", "完成度": 75},
    {"里程碑": "测试验收", "计划日期": "2024-05-31", "实际日期": "-", "状态": "未开始", "完成度": 0}
]

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("project_info", project_info)
generator.add_data_source("milestones", milestones)
generator.save("output/project_report.pdf")
```
