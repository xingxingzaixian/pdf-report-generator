# 图片处理

在 PDF 中插入和调整图片。

## 基本图片

```json
{
  "type": "image",
  "path": "images/photo.png",
  "width": 200,
  "alignment": "center"
}
```

## 图片属性

| 属性 | 类型 | 说明 |
|------|------|------|
| `path` | string | 图片文件路径 |
| `width` | number | 图片宽度（像素） |
| `height` | number | 图片高度（像素） |
| `alignment` | string | 对齐方式：`left` / `center` / `right` |
| `keepAspectRatio` | boolean | 是否保持纵横比（默认 true） |

## 支持的格式

- PNG
- JPEG / JPG
- GIF
- BMP
- TIFF

## 宽高控制

### 固定宽度

```json
{
  "type": "image",
  "path": "images/chart.png",
  "width": 400
}
```

### 固定高度

```json
{
  "type": "image",
  "path": "images/banner.png",
  "height": 100
}
```

### 固定宽高

```json
{
  "type": "image",
  "path": "images/logo.png",
  "width": 150,
  "height": 50,
  "keepAspectRatio": false
}
```

## 在表格中使用图片

```json
{
  "type": "table",
  "dataSource": "products",
  "columns": ["名称", "图片", "价格"],
  "columnWidths": [2, 1.5, 1],
  "imageColumns": {
    "图片": {
      "width": 50,
      "height": 50
    }
  }
}
```

## 常见问题

### 图片不显示

- 检查路径是否正确
- 确认文件存在且可读
- 检查文件格式是否支持

### 图片模糊

- 使用更高分辨率的原图
- PNG 格式通常比 JPEG 更清晰

### 图片过大

- 设置 `width` 和 `height` 调整尺寸
- 使用 `keepAspectRatio: true` 保持比例

## 下一步

- [中文字体](./chinese-fonts.md) - 配置中文字体支持
- [条件渲染](./conditional-rendering.md) - 根据条件显示图片
