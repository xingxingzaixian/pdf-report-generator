# 中文字体说明

## 已包含的字体

此目录包含以下中文字体：

1. **SimHei.TTF** (黑体)
   - 用途：标题、表头、粗体文本
   - 特点：笔画粗壮，适合强调

2. **SimSun.TTF** (宋体)
   - 用途：正文、表格内容
   - 特点：笔画细腻，适合长文本阅读

3. **GB2312.TTF** (GB2312编码字体)
   - 用途：备用字体
   - 特点：兼容性好

## 自动加载

系统会在启动时自动加载`fonts`目录下的字体文件，无需手动配置。

加载顺序：
1. 扫描fonts目录
2. 注册找到的中文字体
3. 设置默认字体为SimHei（黑体）
4. 更新所有默认样式使用中文字体

## 字体优先级

### PDF文本字体
- 优先使用：SimHei（黑体）
- 备选：SimSun（宋体）
- 备选：GB2312

### 表格字体
- 表头：SimHei（黑体，加粗效果）
- 内容：SimSun（宋体，便于阅读）

### 图表字体
matplotlib会自动使用注册的中文字体，优先级：
1. SimHei
2. SimSun
3. GB2312
4. 系统字体（如Microsoft YaHei）

## 添加自定义字体

### 方法1: 放入fonts目录

将.ttf或.TTF字体文件放入此目录，系统会自动识别并注册。

支持的文件名格式：
- SimHei.ttf / SimHei.TTF
- SimSun.ttf / SimSun.TTF
- GB2312.ttf / GB2312.TTF

### 方法2: 手动注册

在代码中手动注册字体：

```python
from pdf_generator import PDFReportGenerator

generator = PDFReportGenerator(config_dict=config)

# 注册自定义字体
generator.style_manager.register_font('MyFont', 'path/to/font.ttf')
```

### 方法3: 配置文件指定

在JSON配置文件的样式中指定字体：

```json
{
  "styles": {
    "custom": {
      "fontName": "SimHei",
      "fontSize": 12
    }
  }
}
```

## 验证字体加载

运行示例代码时，会在控制台输出字体注册信息：

```
Successfully registered font: SimHei from SimHei.TTF
Successfully registered font: SimSun from SimSun.TTF
Successfully registered font: GB2312 from GB2312.TTF
Default Chinese font set to: SimHei
Matplotlib: Registered font SimHei from SimHei.TTF
Matplotlib: Registered font SimSun from SimSun.TTF
Matplotlib: Chinese fonts set to ['SimHei', 'SimSun', 'GB2312']
```

如果看到以上输出，说明字体加载成功！

## 常见问题

### Q: 中文仍然显示为方块？
A: 检查以下几点：
1. 字体文件是否在fonts目录下
2. 文件扩展名是否正确（.ttf或.TTF）
3. 查看控制台是否有字体注册成功的消息

### Q: 想使用其他中文字体？
A: 
1. 将字体文件放入fonts目录
2. 修改`pdf_generator/core/styles.py`中的`font_mappings`
3. 或在配置文件中直接指定fontName

### Q: 如何使用粗体？
A: 在样式配置中设置 `"bold": true`，系统会自动使用SimHei字体

### Q: 字体文件从哪里获取？
A: 
- Windows系统：C:\Windows\Fonts\
- Mac系统：/Library/Fonts/ 或 /System/Library/Fonts/
- Linux系统：/usr/share/fonts/

**注意：使用字体时请遵守相关版权协议**

## 技术说明

### ReportLab字体注册
```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('SimHei', 'fonts/SimHei.TTF'))
```

### Matplotlib字体注册
```python
import matplotlib.font_manager as fm

fm.fontManager.addfont('fonts/SimHei.TTF')
plt.rcParams['font.sans-serif'] = ['SimHei']
```

---

**字体已配置完成，PDF生成服务现已完全支持中文！** ✅

