# 字体配置快速参考

中文字体配置的快速参考指南。

## 🚀 30秒快速配置

### 1. 创建字体目录
```bash
mkdir fonts
```

### 2. 添加字体文件
- **Windows**: 从 `C:\Windows\Fonts\` 复制 `SimHei.ttf` 和 `SimSun.ttf`
- **Linux**: `sudo apt-get install fonts-wqy-microhei`
- **Mac**: 使用系统字体或下载开源字体

### 3. 验证配置
```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict={})
print("已注册字体：", generator.style_manager.registered_fonts)
# 应该输出：{'SimHei', 'SimSun'}
```

## 📝 配置方式对比

| 方式 | 适用场景 | 代码示例 |
|------|---------|----------|
| **自动查找** | 开发环境 | `PDFReportGenerator(config_dict=config)` |
| **参数指定** | 灵活配置 | `PDFReportGenerator(config_dict=config, font_dirs=['./fonts'])` |
| **配置文件** | 生产环境 | `{"metadata": {"fontDirs": ["./fonts"]}}` |

## 🎯 支持的中文字体

| 字体名称 | 文件名 | 推荐用途 |
|---------|--------|----------|
| SimHei  | SimHei.ttf | 标题、强调文本 |
| SimSun  | SimSun.ttf | 正文、段落 |
| GB2312  | GB2312.ttf | 特殊编码需求 |

## 🔧 常用配置

### 基础配置
```python
# 自动查找 fonts/ 目录
generator = PDFReportGenerator(config_dict=config)
```

### 多目录配置
```python
generator = PDFReportGenerator(
    config_dict=config,
    font_dirs=[
        './fonts',                    # 项目字体
        'C:\\Windows\\Fonts',         # Windows 系统字体
        '/usr/share/fonts/chinese',   # Linux 中文字体
    ]
)
```

### 配置文件方式
```json
{
  "metadata": {
    "fontDirs": ["./fonts", "C:\\Windows\\Fonts"]
  }
}
```

## 🚨 常见问题

### Q: 中文显示为方框？
**A**: 字体未加载，检查：
1. `fonts/` 目录是否存在
2. 字体文件是否正确
3. 运行验证代码查看已注册字体

### Q: 如何知道字体是否加载成功？
**A**: 
```python
print(generator.style_manager.registered_fonts)
# 输出：{'SimHei', 'SimSun'} 表示成功
# 输出：set() 表示未加载
```

### Q: 可以不配置中文字体吗？
**A**: 可以！英文内容会正常显示，中文可能显示为方框。

## 📚 详细文档

- [中文字体配置完整指南](./chinese-fonts.md)
- [字体配置指南](../../FONT_CONFIGURATION.md)
- [安装指南](../01-getting-started/installation.md)

---

**上一页**：[中文字体配置](./chinese-fonts.md)  
**下一页**：[图片处理](./images-handling.md)
