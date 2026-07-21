# 部署

## 开发环境

```bash
# 安装依赖
pip install -e .[api]

# 启动开发服务器（热重载）
pdf-report-api --reload
```

## 生产环境

### 使用 gunicorn + uvicorn

```bash
# 安装依赖
pip install pdf-report-generator[api]

# 使用 gunicorn 启动
gunicorn api.main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8080
```

### 使用 Docker

创建 `Dockerfile`：

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["pdf-report-api", "--host", "0.0.0.0", "--port", "8080"]
```

构建并运行：

```bash
docker build -t pdf-report-api .
docker run -p 8080:8080 pdf-report-api
```

### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `HOST` | `0.0.0.0` | 监听地址 |
| `PORT` | `8080` | 监听端口 |
| `WORKERS` | `1` | 工作进程数 |
| `LOG_LEVEL` | `info` | 日志级别 |

## 性能建议

- 生产环境使用多个 worker 进程
- 启用 HTTP 缓存（如 Nginx 反向代理）
- 对重复生成的报告使用缓存
- 考虑使用消息队列处理大批量生成任务

## 下一步

- [Web API 使用](./usage-api.md) - 了解 API 端点
- [PDFReportGenerator API](/api/pdf-report-generator.md) - 查看完整 API 参考
