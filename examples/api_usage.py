"""
PDF Generator API - 使用示例

演示如何使用FastAPI Web服务生成PDF
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import requests
import json

# API基础URL
BASE_URL = "http://localhost:8000"


def example1_generate_from_json():
    """示例1: 通过JSON配置生成PDF"""
    print("示例1: 通过JSON配置生成PDF")
    
    config = {
        "metadata": {
            "title": "API生成的报告",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 20,
                "alignment": "center",
                "bold": True
            }
        },
        "dataSources": [],
        "elements": [
            {
                "type": "text",
                "content": "这是通过API生成的PDF报告",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "text",
                "content": "使用FastAPI Web服务，可以轻松地通过HTTP请求生成PDF。",
                "style": "body"
            }
        ]
    }
    
    # 准备请求数据
    request_data = {
        "config": config,
        "output_filename": "api_report.pdf"
    }
    
    # 发送POST请求
    response = requests.post(
        f"{BASE_URL}/api/generate",
        json=request_data
    )
    
    if response.status_code == 200:
        # 保存PDF文件
        with open("api_generated_report.pdf", "wb") as f:
            f.write(response.content)
        print("✓ PDF生成成功: api_generated_report.pdf\n")
    else:
        print(f"✗ 生成失败: {response.text}\n")


def example2_generate_with_data():
    """示例2: 带数据的PDF生成"""
    print("示例2: 带数据的PDF生成")
    
    config = {
        "metadata": {
            "title": "销售数据报告",
            "pageSize": "A3"
        },
        "styles": {
            "title": {"fontSize": 18, "alignment": "center", "bold": True},
            "tableStyle": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#4472C4",
                "headerTextColor": "#FFFFFF"
            }
        },
        "dataSources": [],
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "title"},
            {"type": "spacer", "height": 0.5},
            {"type": "table", "dataSource": "sales", "style": "tableStyle"},
            {"type": "spacer", "height": 0.5},
            {
                "type": "chart",
                "chartType": "bar",
                "dataSource": "sales",
                "xAxis": "product",
                "yAxis": "sales",
                "title": "Sales by Product",
                "width": 6,
                "height": 4
            }
        ]
    }
    
    # 准备数据
    data = {
        "sales": [
            {"product": "Product A", "sales": 150, "revenue": 45000},
            {"product": "Product B", "sales": 230, "revenue": 69000},
            {"product": "Product C", "sales": 180, "revenue": 54000}
        ]
    }
    
    request_data = {
        "config": config,
        "data": data,
        "output_filename": "sales_report.pdf"
    }
    
    response = requests.post(
        f"{BASE_URL}/api/generate",
        json=request_data
    )
    
    if response.status_code == 200:
        with open("api_sales_report.pdf", "wb") as f:
            f.write(response.content)
        print("✓ PDF生成成功: api_sales_report.pdf\n")
    else:
        print(f"✗ 生成失败: {response.text}\n")


def example3_validate_config():
    """示例3: 验证配置"""
    print("示例3: 验证配置")
    
    config = {
        "metadata": {
            "title": "测试报告",
            "pageSize": "INVALID_SIZE"  # 故意使用无效值
        },
        "elements": [
            {
                "type": "text",
                "content": "测试内容"
            }
        ]
    }
    
    response = requests.post(
        f"{BASE_URL}/api/validate",
        json={"config": config}
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"配置有效性: {result['valid']}")
        if result['errors']:
            print("错误:")
            for error in result['errors']:
                print(f"  - {error}")
        if result['warnings']:
            print("警告:")
            for warning in result['warnings']:
                print(f"  - {warning}")
        print()
    else:
        print(f"✗ 验证失败: {response.text}\n")


def example4_upload_files():
    """示例4: 上传配置和数据文件"""
    print("示例4: 上传文件生成PDF")
    
    # 准备配置文件
    config = {
        "metadata": {"title": "Upload Test"},
        "elements": [
            {"type": "text", "content": "File Upload Test", "style": "title"},
            {"type": "table", "dataSource": "uploaded_data"}
        ]
    }
    
    # 准备数据文件（CSV格式）
    csv_data = "name,value\nItem 1,100\nItem 2,200\nItem 3,150"
    
    files = {
        'config': ('config.json', json.dumps(config), 'application/json'),
        'data': ('data.csv', csv_data, 'text/csv')
    }
    
    response = requests.post(
        f"{BASE_URL}/api/generate/upload",
        files=files
    )
    
    if response.status_code == 200:
        with open("api_uploaded_report.pdf", "wb") as f:
            f.write(response.content)
        print("✓ PDF生成成功: api_uploaded_report.pdf\n")
    else:
        print(f"✗ 生成失败: {response.text}\n")


def check_api_status():
    """检查API状态"""
    print("检查API状态...")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✓ API状态: {data['status']}")
            print(f"  版本: {data['version']}")
            print(f"  消息: {data['message']}\n")
            return True
        else:
            print("✗ API未响应\n")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ 无法连接到API服务")
        print("  请确保API服务正在运行: python -m api.main\n")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("PDF Generator API - 使用示例")
    print("=" * 60 + "\n")
    
    # 检查API状态
    if check_api_status():
        # 运行示例
        example1_generate_from_json()
        example2_generate_with_data()
        example3_validate_config()
        example4_upload_files()
        
        print("=" * 60)
        print("所有示例执行完成！")
        print("=" * 60)
    else:
        print("\n请先启动API服务：")
        print("  python -m api.main")
        print("或者：")
        print("  uvicorn api.main:app --reload")

