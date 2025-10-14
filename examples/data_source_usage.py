"""
PDF Generator - 数据源使用示例

演示如何使用PDF生成器的数据源功能
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pdf_generator import PDFReportGenerator

# 示例1: 使用CSV数据源
def example1_csv_data():
    """使用CSV文件作为数据源"""
    print("示例1: 使用CSV文件作为数据源")
    
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
            },
            "table": {
                "gridColor": "#CCCCCC",
                "headerBackgroundColor": "#4472C4",
                "alternateRowColor": "#F2F2F2",
                "padding": 8
            }
        },
        "dataSources": [
          {
            "name": "sales_data",
            "type": "csv",
            "path": "data/sales.csv"
          }
        ],
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
                "content": "这是报告的正文内容。读取CSV文件的数据，并生成表格。",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.1
            },
            {
                "type": "table",
                "dataSource": "sales_data",
                "style": "table"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/data_source_csv_data_report.pdf")
    print("✓ 生成成功: examples/data_source_csv_data_report.pdf\n")


# 示例2: 使用JSON数据源
def example2_json_data():
    """使用JSON文件作为数据源"""
    print("示例2: 使用JSON文件作为数据源")
    
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
            }
        },
        "dataSources": [
          {
            "name": "expenses_data",
            "type": "json",
            "path": "data/expenses.json"
          }
        ],
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
                "content": "这是报告的正文内容。读取JSON文件的数据，并生成图表。",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.1
            },
            {
                "type": "chart",
                "dataSource": "expenses_data",
                "chartType": "bar",
                "xAxis": "类别",
                "yAxis": "金额",
                "title": "支出分布",
                "width": 6.5,
                "height": 4
            }
        ]
    }

    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/data_source_json_data_report.pdf")
    print("✓ 生成成功: examples/data_source_json_data_report.pdf\n")


# 示例3: 使用Excel数据源
def example3_excel_data():
    """使用API作为数据源"""
    print("示例3: 使用Excel作为数据源")
    
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
            },
            "table": {
                "gridColor": "#CCCCCC",
                "headerBackgroundColor": "#4472C4",
                "alternateRowColor": "#F2F2F2",
                "padding": 8
            }
        },
        "dataSources": [
          {
            "name": "sales_data",
            "type": "excel",
            "path": "data/sales.xlsx"
          }
        ],
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
                "content": "这是报告的正文内容。读取Excel文件的数据，并生成表格。",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.1
            },
            {
                "type": "table",
                "dataSource": "sales_data",
                "style": "table"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/data_source_excel_data_report.pdf")
    print("✓ 生成成功: examples/data_source_excel_data_report.pdf\n")


# 示例4: 使用API数据源
def example4_api_data():
    """使用API作为数据源"""
    print("示例4: 使用API作为数据源")
    
    config = {
        "metadata": {
            "title": "简单报告",
            "pageSize": "A4",
            "orientation": "portrait"
        },
        "dataSources": [
          {
            "name": "api_data",
            "type": "api",
            "url": "http://192.168.10.212:15000/tool/metricConfig/"
          }
        ],
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
                "content": "这是报告的正文内容。读取API的数据，并生成表格。",
                "style": "body"
            },
            {
                "type": "spacer",
                "height": 0.1
            },
            {
                "type": "table",
                "dataSource": "api_data",
                "style": "table",
                "columns": ["metric_id", "metric_name", "description"],
                "columnWidths": [1.2, 1.5, 3.8],
                "wrapColumns": [0, 1, 2],  # description列（索引2）自动换行
                "wrapThreshold": 30  # 超过30个字符自动换行
            }
        ]
    }
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/data_source_api_data_report.pdf")
    print("✓ 生成成功: examples/data_source_api_data_report.pdf\n")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF Generator - 数据源使用示例")
    print("=" * 60 + "\n")

    example1_csv_data()
    example2_json_data()
    example3_excel_data()
    example4_api_data()