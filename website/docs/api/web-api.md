# Web API 端点

启动服务后，所有端点的基础路径为 `http://localhost:8080`。

## 端点列表

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 服务状态 |
| POST | `/api/generate` | 生成 PDF（JSON 配置） |
| POST | `/api/generate/upload` | 生成 PDF（文件上传） |
| POST | `/api/validate` | 验证配置 |
| GET | `/api/templates` | 获取模板列表 |
| GET | `/api/health` | 健康检查 |

## 端点详情

### GET /

服务状态检查。

**响应**:
```json
{
  "status": "running",
  "version": "0.1.1"
}
```

### POST /api/generate

通过 JSON 配置生成 PDF。

**请求体**:
```json
{
  "config": {
    "metadata": {"title": "报告标题"},
    "elements": [
      {"type": "text", "content": "Hello World!"}
    ]
  }
}
```

**响应**: PDF 文件（二进制流）

**Content-Type**: `application/pdf`

### POST /api/generate/upload

通过上传配置文件生成 PDF。

**请求**: `multipart/form-data`

| 字段 | 类型 | 说明 |
|------|------|------|
| `config_file` | file | JSON 配置文件 |

**响应**: PDF 文件（二进制流）

### POST /api/validate

验证 JSON 配置是否合法。

**请求体**:
```json
{
  "config": {
    "metadata": {"title": "测试"},
    "elements": []
  }
}
```

**响应**:
```json
{
  "valid": true,
  "errors": []
}
```

### GET /api/templates

获取可用模板列表。

**响应**:
```json
{
  "templates": [
    {
      "name": "sales_report",
      "description": "销售报告模板",
      "path": "templates/sales_report.json"
    }
  ]
}
```

### GET /api/health

健康检查端点。

**响应**:
```json
{
  "status": "healthy"
}
```

## 错误响应

所有端点在出错时返回：

```json
{
  "detail": "错误描述信息"
}
```

常见 HTTP 状态码：

| 状态码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
