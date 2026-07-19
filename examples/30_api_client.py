"""
30 - API 客户端：通过 HTTP API 调用生成 PDF

演示通过 FastAPI Web 服务生成 PDF 的完整流程。
需要先启动 API 服务器: uv run uvicorn pdf_generator.api.main:app --reload
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import requests
import json

BASE_URL = "http://localhost:8000"


def check_status():
    """检查 API 服务状态"""
    try:
        resp = requests.get(f"{BASE_URL}/")
        if resp.status_code == 200:
            data = resp.json()
            print(f"✅ API 状态: {data['status']}")
            print(f"   版本: {data['version']}")
            print(f"   消息: {data['message']}")
            return True
    except requests.exceptions.ConnectionError:
        pass
    print("❌ 无法连接到 API 服务")
    print("   请先启动: uv run uvicorn pdf_generator.api.main:app --reload")
    return False


def example1_generate_simple():
    """示例1: JSON 配置生成 PDF"""
    print("\n--- 示例1: JSON 配置生成 PDF ---")

    config = {
        "metadata": {"title": "API 生成的报告"},
        "elements": [
            {"type": "text", "content": "通过 API 生成的 PDF", "style": "Title"},
            {"type": "spacer", "height": 0.3},
            {"type": "text", "content": "使用 POST /api/generate 端点，传入 JSON 配置即可生成 PDF。"},
        ]
    }

    resp = requests.post(f"{BASE_URL}/api/generate", json={
        "config": config,
        "output_filename": "api_simple.pdf"
    })

    if resp.status_code == 200:
        path = "examples/output/30_api_simple.pdf"
        with open(path, "wb") as f:
            f.write(resp.content)
        print(f"✅ 已生成: {path}")
    else:
        print(f"❌ 失败: {resp.text}")


def example2_generate_with_data():
    """示例2: 带数据的 PDF 生成"""
    print("\n--- 示例2: 带数据生成 PDF ---")

    config = {
        "metadata": {"title": "API - 数据报告"},
        "styles": {
            "table": {"gridColor": "#CCCCCC", "headerBackground": "#4472C4",
                      "headerTextColor": "#FFFFFF", "fontSize": 10, "padding": 8}
        },
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
            {"type": "spacer", "height": 0.2},
            {"type": "table", "dataSource": "products", "style": "table"},
        ]
    }

    data = {
        "products": [
            {"产品": "笔记本", "销量": 450, "单价": 5999},
            {"产品": "台式机", "销量": 320, "单价": 4299},
            {"产品": "平板", "销量": 580, "单价": 2999},
        ]
    }

    resp = requests.post(f"{BASE_URL}/api/generate", json={
        "config": config,
        "data": data,
        "output_filename": "api_data.pdf"
    })

    if resp.status_code == 200:
        path = "examples/output/30_api_data.pdf"
        with open(path, "wb") as f:
            f.write(resp.content)
        print(f"✅ 已生成: {path}")
    else:
        print(f"❌ 失败: {resp.text}")


def example3_validate():
    """示例3: 配置验证"""
    print("\n--- 示例3: 配置验证 ---")

    # 有效配置
    resp1 = requests.post(f"{BASE_URL}/api/validate", json={
        "config": {"metadata": {"title": "Test"}, "elements": []}
    })
    print(f"有效配置验证: {resp1.json()}")

    # 无效配置
    resp2 = requests.post(f"{BASE_URL}/api/validate", json={
        "config": {"metadata": {"title": "Test", "pageSize": "INVALID"}}
    })
    result = resp2.json()
    print(f"无效配置验证: valid={result.get('valid')}, errors={result.get('errors')}")


def example4_upload():
    """示例4: 文件上传生成 PDF"""
    print("\n--- 示例4: 文件上传生成 PDF ---")

    config = {
        "metadata": {"title": "Upload Test"},
        "elements": [
            {"type": "text", "content": "File Upload Test", "style": "Title"},
            {"type": "table", "dataSource": "uploaded_data"}
        ]
    }

    csv_data = "name,value\nItem1,100\nItem2,200\nItem3,150"

    resp = requests.post(f"{BASE_URL}/api/generate/upload", files={
        "config": ("config.json", json.dumps(config), "application/json"),
        "data": ("data.csv", csv_data, "text/csv")
    })

    if resp.status_code == 200:
        path = "examples/output/30_api_upload.pdf"
        with open(path, "wb") as f:
            f.write(resp.content)
        print(f"✅ 已生成: {path}")
    else:
        print(f"❌ 失败: {resp.text}")


def example5_health_and_templates():
    """示例5: 健康检查 + 模板列表"""
    print("\n--- 示例5: 健康检查 + 模板列表 ---")

    resp = requests.get(f"{BASE_URL}/api/health")
    print(f"健康检查: {resp.json()}")

    resp = requests.get(f"{BASE_URL}/api/templates")
    templates = resp.json()
    print(f"可用模板: {list(templates.keys())}")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF Report Generator - API 客户端示例")
    print("=" * 60)

    if not check_status():
        sys.exit(1)

    example1_generate_simple()
    example2_generate_with_data()
    example3_validate()
    example4_upload()
    example5_health_and_templates()

    print("\n" + "=" * 60)
    print("所有 API 示例执行完成！")
    print("=" * 60)
