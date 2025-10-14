"""运行所有示例的脚本"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from pdf_generator import PDFReportGenerator
import pandas as pd

print("=" * 70)
print("PDF Report Generator - 示例演示")
print("=" * 70)
print()

# 示例1: 简单文本报告
print("示例1: 简单文本报告")
print("-" * 70)

config1 = {
    "metadata": {
        "title": "简单报告示例",
        "pageSize": "A4",
        "orientation": "portrait"
    },
    "styles": {
        "title": {
            "fontSize": 24,
            "textColor": "#2C3E50",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 20
        },
        "body": {
            "fontSize": 11,
            "textColor": "#34495E",
            "alignment": "justify"
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "PDF报告生成服务示例",
            "style": "title"
        },
        {
            "type": "spacer",
            "height": 0.5
        },
        {
            "type": "text",
            "content": "这是一个通过JSON配置生成的PDF文档示例。本系统支持灵活的配置方式，可以轻松创建包含文本、表格、图表和图片的专业报告。",
            "style": "body"
        }
    ]
}

try:
    generator1 = PDFReportGenerator(config_dict=config1)
    generator1.save("smaple_01_simple.pdf")
    print("✓ 成功生成: smaple_01_simple.pdf")
except Exception as e:
    print(f"✗ 生成失败: {e}")

print()

# 示例2: 数据表格
print("示例2: 数据表格报告")
print("-" * 70)

sales_data = pd.DataFrame({
    "产品": ["笔记本电脑", "台式机", "平板电脑", "手机", "配件"],
    "销量": [450, 320, 580, 1200, 890],
    "单价": [5999, 4299, 2999, 3499, 299],
    "销售额": [2699550, 1375680, 1739420, 4198800, 266110]
})

config2 = {
    "metadata": {
        "title": "产品销售数据报告",
        "pageSize": "A4"
    },
    "styles": {
        "title": {
            "fontSize": 20,
            "textColor": "#1A5490",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 25
        },
        "heading": {
            "fontSize": 14,
            "textColor": "#2E5C8A",
            "bold": True,
            "spaceBefore": 15,
            "spaceAfter": 10
        },
        "salesTable": {
            "gridColor": "#BDC3C7",
            "headerBackground": "#3498DB",
            "headerTextColor": "#FFFFFF",
            "fontSize": 10,
            "padding": 8
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "{{metadata.title}}",
            "style": "title"
        },
        {
            "type": "text",
            "content": "销售数据总览",
            "style": "heading"
        },
        {
            "type": "table",
            "dataSource": "sales",
            "style": "salesTable",
            "columnWidths": [2, 1.2, 1.2, 1.5]
        }
    ]
}

try:
    generator2 = PDFReportGenerator(config_dict=config2)
    generator2.add_data_source("sales", sales_data)
    generator2.save("smaple_02_table.pdf")
    print("✓ 成功生成: smaple_02_table.pdf")
except Exception as e:
    print(f"✗ 生成失败: {e}")

print()

# 示例3: 图表报告
print("示例3: 图表报告")
print("-" * 70)

config3 = {
    "metadata": {
        "title": "销售分析图表",
        "pageSize": "A4"
    },
    "styles": {
        "title": {
            "fontSize": 20,
            "alignment": "center",
            "bold": True,
            "spaceAfter": 20
        },
        "heading": {
            "fontSize": 14,
            "bold": True,
            "spaceBefore": 15,
            "spaceAfter": 10
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "{{metadata.title}}",
            "style": "title"
        },
        {
            "type": "text",
            "content": "产品销量对比",
            "style": "heading"
        },
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销量",
            "title": "各产品销量对比（件）",
            "width": 6.5,
            "height": 4,
            "grid": True,
            "alignment": "center"
        },
        {
            "type": "spacer",
            "height": 0.5
        },
        {
            "type": "text",
            "content": "销售额趋势",
            "style": "heading"
        },
        {
            "type": "chart",
            "chartType": "line",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销售额",
            "title": "各产品销售额（元）",
            "width": 6.5,
            "height": 4,
            "grid": True,
            "alignment": "center"
        }
    ]
}

try:
    generator3 = PDFReportGenerator(config_dict=config3)
    generator3.add_data_source("sales", sales_data)
    generator3.save("smaple_03_charts.pdf")
    print("✓ 成功生成: smaple_03_charts.pdf")
except Exception as e:
    print(f"✗ 生成失败: {e}")

print()

# 示例4: 综合报告
print("示例4: 综合报告（文本+表格+图表）")
print("-" * 70)

config4 = {
    "metadata": {
        "title": "2024年度销售分析报告",
        "author": "销售部",
        "pageSize": "A4"
    },
    "styles": {
        "title": {
            "fontSize": 22,
            "textColor": "#2C3E50",
            "alignment": "center",
            "bold": True,
            "spaceAfter": 30
        },
        "heading1": {
            "fontSize": 16,
            "textColor": "#34495E",
            "bold": True,
            "spaceBefore": 20,
            "spaceAfter": 12
        },
        "heading2": {
            "fontSize": 13,
            "textColor": "#7F8C8D",
            "bold": True,
            "spaceBefore": 15,
            "spaceAfter": 8
        },
        "body": {
            "fontSize": 10,
            "textColor": "#2C3E50",
            "alignment": "justify",
            "spaceAfter": 10
        },
        "dataTable": {
            "gridColor": "#BDC3C7",
            "headerBackground": "#3498DB",
            "headerTextColor": "#FFFFFF",
            "fontSize": 9,
            "padding": 6
        }
    },
    "elements": [
        {
            "type": "text",
            "content": "{{metadata.title}}",
            "style": "title"
        },
        {
            "type": "text",
            "content": "报告生成日期：2024年12月",
            "style": "body"
        },
        {
            "type": "spacer",
            "height": 0.8
        },
        {
            "type": "text",
            "content": "一、概述",
            "style": "heading1"
        },
        {
            "type": "text",
            "content": "本报告汇总了2024年度各产品线的销售数据，包括销量、销售额等关键业绩指标。通过数据分析，我们可以清晰地了解各产品的市场表现，为下一年度的销售策略制定提供数据支持。",
            "style": "body"
        },
        {
            "type": "text",
            "content": "二、销售数据",
            "style": "heading1"
        },
        {
            "type": "text",
            "content": "2.1 销售明细表",
            "style": "heading2"
        },
        {
            "type": "table",
            "dataSource": "sales",
            "style": "dataTable"
        },
        {
            "type": "spacer",
            "height": 0.5
        },
        {
            "type": "text",
            "content": "2.2 销量对比分析",
            "style": "heading2"
        },
        {
            "type": "chart",
            "chartType": "bar",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销量",
            "title": "各产品销量对比图",
            "width": 6.5,
            "height": 3.5,
            "grid": True
        },
        {
            "type": "pagebreak"
        },
        {
            "type": "text",
            "content": "三、趋势分析",
            "style": "heading1"
        },
        {
            "type": "text",
            "content": "3.1 销售额走势",
            "style": "heading2"
        },
        {
            "type": "chart",
            "chartType": "line",
            "dataSource": "sales",
            "xAxis": "产品",
            "yAxis": "销售额",
            "title": "销售额趋势图",
            "width": 6.5,
            "height": 4,
            "grid": True
        },
        {
            "type": "spacer",
            "height": 0.5
        },
        {
            "type": "text",
            "content": "四、结论与建议",
            "style": "heading1"
        },
        {
            "type": "text",
            "content": "根据以上数据分析，我们建议在下一年度加强手机和平板电脑产品线的市场推广，同时优化笔记本和台式机的产品定位，以提升整体销售业绩。",
            "style": "body"
        }
    ]
}

try:
    generator4 = PDFReportGenerator(config_dict=config4)
    generator4.add_data_source("sales", sales_data)
    generator4.save("smaple_04_comprehensive.pdf")
    print("✓ 成功生成: smaple_04_comprehensive.pdf")
except Exception as e:
    print(f"✗ 生成失败: {e}")

print()
print("=" * 70)
print("所有示例执行完成！")
print("=" * 70)
print("\n生成的文件：")
print("  - smaple_01_simple.pdf")
print("  - smaple_02_table.pdf")
print("  - smaple_03_charts.pdf")
print("  - smaple_04_comprehensive.pdf")
print("\n您可以打开这些PDF文件查看效果。")

