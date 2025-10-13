"""
PDF Generator - 独立使用示例

演示如何将PDF生成器作为Python库使用
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pdf_generator import PDFReportGenerator
import pandas as pd

# 示例1: 从配置文件生成PDF
def example1_from_config():
    """从JSON配置文件生成PDF"""
    print("示例1: 从配置文件生成PDF")
    
    generator = PDFReportGenerator(config_path="templates/sales_report.json")
    generator.save("output_sales_report.pdf")
    print("✓ 生成成功: output_sales_report.pdf\n")


# 示例2: 使用字典配置生成PDF
def example2_from_dict():
    """使用配置字典生成PDF"""
    print("示例2: 使用字典配置生成PDF")
    
    config = {
        "metadata": {
            "title": "简单报告",
            "pageSize": "A4",
            "orientation": "portrait"
        },
        "styles": {
            "title": {
                "fontSize": 20,
                "textColor": "#333333",
                "alignment": "center",
                "bold": True
            },
            "body": {
                "fontSize": 10,
                "textColor": "#666666"
            }
        },
        "dataSources": [],
        "elements": [
            {
                "type": "text",
                "content": "这是一个简单的PDF报告",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "text",
                "content": "这是报告的正文内容。可以包含多行文本和各种格式。",
                "style": "body"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_simple_report.pdf")
    print("✓ 生成成功: output_simple_report.pdf\n")


# 示例3: 动态添加数据源
def example3_dynamic_data():
    """动态添加数据并生成PDF"""
    print("示例3: 动态添加数据源")
    
    # 创建示例数据
    sales_data = pd.DataFrame({
        "产品": ["产品A", "产品B", "产品C", "产品D"],
        "销量": [150, 230, 180, 200],
        "金额": [45000, 69000, 54000, 60000],
        "增长率": ["15%", "23%", "8%", "12%"]
    })
    
    config = {
        "metadata": {
            "title": "动态数据报告",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 18,
                "alignment": "center",
                "bold": True
            },
            "dataTable": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#4472C4",
                "headerTextColor": "#FFFFFF",
                "fontSize": 9
            }
        },
        "dataSources": [],
        "elements": [
            {
                "type": "text",
                "content": "销售数据报告",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.5
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
                "type": "chart",
                "chartType": "bar",
                "dataSource": "sales",
                "xAxis": "产品",
                "yAxis": "销量",
                "title": "产品销量对比",
                "width": 6,
                "height": 4
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.add_data_source("sales", sales_data)
    generator.save("output_dynamic_data.pdf")
    print("✓ 生成成功: output_dynamic_data.pdf\n")


# 示例4: 图片元素示例
def example4_image():
    """演示如何在PDF中插入图片"""
    print("示例4: 图片元素示例")
    
    # 首先创建demo.png图片（如果不存在）
    import os
    if not os.path.exists("demo.png"):
        try:
            from PIL import Image, ImageDraw, ImageFont
            img = Image.new('RGB', (400, 200), color='#3498DB')
            draw = ImageDraw.Draw(img)
            draw.rectangle([10, 10, 390, 190], outline='white', width=3)
            try:
                font = ImageFont.truetype("arial.ttf", 32)
            except:
                font = ImageFont.load_default()
            draw.text((200, 80), "PDF Generator", fill='white', anchor="mm", font=font)
            draw.text((200, 120), "Demo Image", fill='white', anchor="mm", font=font)
            img.save('demo.png')
            print("  ✓ 创建demo.png图片")
        except Exception as e:
            print(f"  ⚠ 无法创建demo.png: {e}")
            print("  跳过图片示例\n")
            return
    
    config = {
        "metadata": {
            "title": "图片插入示例",
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
            },
            "body": {
                "fontSize": 10,
                "spaceAfter": 8
            }
        },
        "dataSources": [],
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "text",
                "content": "一、居中对齐的图片",
                "style": "heading"
            },
            {
                "type": "text",
                "content": "以下是一张居中对齐的示例图片，宽度设置为200像素，保持宽高比：",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "image",
                "path": "demo.png",
                "width": 550,
                "height": 225,
                "alignment": "center",
                "keepAspectRatio": False
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "text",
                "content": "二、左对齐的图片",
                "style": "heading"
            },
            {
                "type": "text",
                "content": "同样的图片，左对齐显示，宽度200像素，高度100像素：",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "image",
                "path": "demo.png",
                "width": 200,
                "height": 100,
                "alignment": "left",
                "keepAspectRatio": False
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "text",
                "content": "三、右对齐的小图片",
                "style": "heading"
            },
            {
                "type": "text",
                "content": "图片右对齐显示，尺寸150x75：",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "image",
                "path": "demo.png",
                "width": 150,
                "height": 75,
                "alignment": "right",
                "keepAspectRatio": False
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_image_demo.pdf")
    print("✓ 生成成功: output_image_demo.pdf\n")


# 示例5: 复杂报告（多种元素类型）
def example5_complex():
    """生成包含多种元素的复杂报告"""
    print("示例5: 复杂报告")
    
    # 准备数据
    data = pd.DataFrame({
        "月份": ["1月", "2月", "3月", "4月"],
        "收入": [100000, 120000, 115000, 130000],
        "支出": [80000, 85000, 90000, 88000],
        "利润": [20000, 35000, 25000, 42000]
    })
    
    config = {
        "metadata": {
            "title": "月度财务报告",
            "author": "财务部",
            "pageSize": "A4",
            "orientation": "portrait"
        },
        "styles": {
            "title": {"fontSize": 22, "alignment": "center", "bold": True},
            "heading": {"fontSize": 14, "bold": True, "spaceBefore": 15},
            "body": {"fontSize": 10},
            "table1": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#2E75B6",
                "headerTextColor": "#FFFFFF"
            }
        },
        "dataSources": [],
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "title"},
            {"type": "spacer", "height": 0.5},
            {"type": "text", "content": "报告概述", "style": "heading"},
            {"type": "text", "content": "本报告展示了最近4个月的财务数据，包括收入、支出和利润情况。", "style": "body"},
            {"type": "spacer", "height": 0.3},
            {"type": "text", "content": "数据表格", "style": "heading"},
            {"type": "table", "dataSource": "finance", "style": "table1"},
            {"type": "spacer", "height": 0.5},
            {"type": "text", "content": "收入趋势", "style": "heading"},
            {
                "type": "chart",
                "chartType": "line",
                "dataSource": "finance",
                "xAxis": "月份",
                "yAxis": ["收入", "支出", "利润"],
                "title": "财务趋势图",
                "width": 6.5,
                "height": 4
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.add_data_source("finance", data)
    generator.save("output_complex_report.pdf")
    print("✓ 生成成功: output_complex_report.pdf\n")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF Generator - 使用示例")
    print("=" * 60 + "\n")
    
    # 运行所有示例
    # example1_from_config()  # 需要配置文件
    example2_from_dict()
    example3_dynamic_data()
    example4_image()
    example5_complex()
    
    print("=" * 60)
    print("所有示例执行完成！")
    print("=" * 60)

