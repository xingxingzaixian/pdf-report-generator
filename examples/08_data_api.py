"""
08 - API 数据源：从 HTTP API 获取数据生成报告

演示 dataSources 配置中 type: api 的使用方式。
配置中的 URL 需要替换为实际可用的 API 地址。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "API 数据源示例"},
    "styles": {
        "apiTable": {
            "gridColor": "#CCCCCC",
            "headerBackground": "#1ABC9C",
            "headerTextColor": "#FFFFFF",
            "fontSize": 9,
            "padding": 6
        }
    },
    "dataSources": [
        {
            "name": "api_data",
            "type": "api",
            "url": "http://192.168.10.212:15000/tool/metricConfig/"
        }
    ],
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "数据来源: HTTP API（需要网络连接）"},
        {"type": "text", "content": "URL: http://192.168.10.212:15000/tool/metricConfig/"},
        {"type": "spacer", "height": 0.2},
        {
            "type": "table",
            "dataSource": "api_data",
            "style": "apiTable",
            "columns": ["metric_id", "metric_name", "description"],
            "columnWidths": [1.2, 1.5, 3.8],
            "wrapColumns": [0, 1, 2],
            "wrapThreshold": 30
        },
    ]
}

try:
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/output/08_data_api.pdf")
    print("✅ 已生成: examples/output/08_data_api.pdf")
except Exception as e:
    print(f"⚠️  API 数据源连接失败（网络不可达）: {e}")
    print("   这是正常现象，API 示例需要内网环境。")
