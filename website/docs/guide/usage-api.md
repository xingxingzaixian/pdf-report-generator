# Web API 使用

## 启动服务

### 方式 1: 命令行启动

```bash
# 安装 API 依赖
pip install pdf-report-generator[api]

# 启动服务
pdf-report-api --host localhost --port 8080

# 开发模式（热重载）
pdf-report-api --reload

# 生产模式（多进程）
pdf-report-api --workers 4
```

### 方式 2: Python 代码启动

```python
from pdf_generator import start_api_server

start_api_server(host="localhost", port=8080)
```

### 方式 3: uvicorn 直接启动

```bash
python -m api.main
# 或
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

## API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 服务状态 |
| POST | `/api/generate` | 生成 PDF（JSON 配置） |
| POST | `/api/generate/upload` | 生成 PDF（文件上传） |
| POST | `/api/validate` | 验证配置 |
| GET | `/api/templates` | 获取模板列表 |
| GET | `/api/health` | 健康检查 |

## 使用示例

### 通过 Python requests

```python
import requests

config = {
    "metadata": {"title": "API 报告"},
    "elements": [
        {"type": "text", "content": "通过 API 生成的 PDF"}
    ]
}

response = requests.post(
    "http://localhost:8080/api/generate",
    json={"config": config}
)

with open("output.pdf", "wb") as f:
    f.write(response.content)
```

### 通过 curl

```bash
curl -X POST http://localhost:8080/api/generate \
  -H "Content-Type: application/json" \
  -d '{"config": {"metadata": {"title": "Test"}, "elements": [{"type": "text", "content": "Hello"}]}}' \
  --output output.pdf
```

## API 文档

启动服务后，访问以下地址查看完整 API 文档：

- **Swagger UI**: http://localhost:8080/docs
- **ReDoc**: http://localhost:8080/redoc

## 下一步

- [PDFReportGenerator API](/api/pdf-report-generator.md) - 查看完整 API 参考
- [配置 Schema](/api/configuration-schema.md) - 了解配置的完整结构
