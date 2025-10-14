# PDF报告生成器 - 完整文档

欢迎使用PDF报告生成器的完整中文文档！这是一个强大、灵活的PDF报告生成系统，支持通过JSON配置文件定义报告格式，自动从多种数据源获取数据并生成专业的PDF文档。

## 📚 文档导航

### 🚀 [1. 入门指南](./01-getting-started/)

快速上手PDF报告生成器：

- **[安装指南](./01-getting-started/installation.md)** - 环境准备、依赖安装、字体配置
- **[快速开始](./01-getting-started/quick-start.md)** - 5分钟生成第一个PDF报告
- **[创建第一个完整报告](./01-getting-started/first-report.md)** - 分步教程
- **[部署指南](./01-getting-started/deployment.md)** - 本地部署、服务器部署、Docker部署

### 📖 [2. 用户手册](./02-user-guide/)

完整的功能使用说明：

- **[基本概念](./02-user-guide/basic-concepts.md)** - 理解配置驱动、数据源、元素等核心概念
- **[配置文件总览](./02-user-guide/configuration-overview.md)** - JSON配置结构详解
- **[数据源详解](./02-user-guide/data-sources.md)** - JSON、CSV、Excel、API、数据库
- **[样式系统](./02-user-guide/styles.md)** - 自定义段落和表格样式
- **[模板变量](./02-user-guide/templates.md)** - Jinja2模板语法和变量替换

#### 元素详解
- **[文本元素](./02-user-guide/elements/text.md)** - 段落、标题、格式化文本
- **[表格元素](./02-user-guide/elements/table.md)** - 数据表格、样式定制
- **[图表元素](./02-user-guide/elements/chart.md)** - 柱状图、折线图、饼图等
- **[图片元素](./02-user-guide/elements/image.md)** - 图片插入和配置
- **[其他元素](./02-user-guide/elements/others.md)** - 分页符、间隔、列表等

### ⭐ [3. 高级功能](./03-advanced-features/)

掌握高级特性：

- **[页眉页脚](./03-advanced-features/headers-footers.md)** - 三栏布局、变量替换、样式配置
- **[自动目录](./03-advanced-features/table-of-contents.md)** - 多级目录、自动生成、超链接
- **[封面设计](./03-advanced-features/cover-pages.md)** - 背景图片/渐变、元素布局、预设模板
- **[表格合并](./03-advanced-features/table-merging.md)** - 单元格合并的高级用法
- **[中文字体](./03-advanced-features/chinese-fonts.md)** - 字体配置、Matplotlib中文显示 ⭐ **重要**
- **[图片处理](./03-advanced-features/images-handling.md)** - 高级图片处理技巧
- **[页码格式](./03-advanced-features/page-numbers.md)** - 阿拉伯、罗马、中文数字
- **[书签和链接](./03-advanced-features/bookmarks-links.md)** - PDF书签、超链接跳转

### 🔧 [4. API参考](./04-api-reference/)

完整的编程接口文档：

#### Python API
- **[PDFReportGenerator类](./04-api-reference/python-api/generator.md)** - 主生成器类
- **[ConfigParser类](./04-api-reference/python-api/config-parser.md)** - 配置解析器
- **[数据源类](./04-api-reference/python-api/data-sources.md)** - 所有数据源类
- **[元素工厂类](./04-api-reference/python-api/elements.md)** - 元素创建和管理
- **[工具函数](./04-api-reference/python-api/utilities.md)** - 辅助工具函数

#### 其他API
- **[Web API](./04-api-reference/web-api.md)** - FastAPI REST接口详解
- **[配置Schema](./04-api-reference/configuration-schema.md)** - 完整JSON Schema参考

### 💡 [5. 示例库](./05-examples/)

丰富的实例代码：

- **[基础示例](./05-examples/simple-examples.md)** - 简单示例集合
- **[图表示例](./05-examples/chart-examples.md)** - 各类图表示例
- **[表格示例](./05-examples/table-examples.md)** - 表格应用示例
- **[完整报告](./05-examples/complete-report.md)** - 综合完整示例
- **[API使用示例](./05-examples/api-usage.md)** - Web API调用示例

#### 业务报告示例
- **[销售报告](./05-examples/business-reports/sales-report.md)** - 销售数据分析报告
- **[财务报告](./05-examples/business-reports/financial-report.md)** - 财务报表生成
- **[数据分析报告](./05-examples/business-reports/analysis-report.md)** - 数据分析和可视化

### 🛠️ [6. 开发文档](./06-development/)

面向开发者的技术文档：

- **[系统架构](./06-development/architecture.md)** - 整体架构设计
- **[代码结构](./06-development/code-structure.md)** - 项目代码组织
- **[测试指南](./06-development/testing.md)** - 单元测试和集成测试
- **[故障排查](./06-development/troubleshooting.md)** - 常见问题解决
- **[贡献指南](./06-development/contributing.md)** - 如何参与开发

#### 扩展开发
- **[自定义元素](./06-development/extending/custom-elements.md)** - 开发新的PDF元素类型
- **[自定义数据源](./06-development/extending/custom-data-sources.md)** - 实现新的数据源
- **[自定义样式](./06-development/extending/custom-styles.md)** - 创建自定义样式

### 📋 [7. 附录](./07-appendix/)

补充资料和参考：

- **[常见问题](./07-appendix/faq.md)** - FAQ汇总
- **[术语表](./07-appendix/glossary.md)** - 专业术语解释
- **[更新日志](./07-appendix/changelog.md)** - 版本更新记录
- **[相关资源](./07-appendix/resources.md)** - 外部链接和资源
- **[配置示例集](./07-appendix/configuration-examples/)** - 完整配置文件示例

## 🎯 快速链接

### 我想...

- **快速生成第一个PDF** → [快速开始](./01-getting-started/quick-start.md)
- **理解配置文件格式** → [配置文件总览](./02-user-guide/configuration-overview.md)
- **添加图表到报告** → [图表元素](./02-user-guide/elements/chart.md)
- **设置页眉页脚** → [页眉页脚](./03-advanced-features/headers-footers.md)
- **生成带目录的报告** → [自动目录](./03-advanced-features/table-of-contents.md)
- **解决中文显示问题** → [中文字体](./03-advanced-features/chinese-fonts.md)
- **使用Web API** → [Web API](./04-api-reference/web-api.md)
- **查看完整示例** → [示例库](./05-examples/)
- **开发自定义功能** → [扩展开发](./06-development/extending/)

## 📦 项目特性

### 核心功能
- ✅ JSON配置驱动的报告生成
- ✅ 多种数据源支持（JSON、CSV、Excel、API、数据库）
- ✅ 丰富的PDF元素（文本、表格、图表、图片）
- ✅ 完全可定制的样式系统
- ✅ Python库和Web API两种使用方式
- ✅ Jinja2模板变量支持

### 高级特性
- ✅ 页眉页脚（三栏布局、变量替换）
- ✅ 自动目录生成（多级、可点击）
- ✅ 封面页设计（背景、预设模板）
- ✅ 表格单元格合并
- ✅ 完整的中文支持
- ✅ 多种页码格式
- ✅ PDF书签和超链接

## 💬 获取帮助

- **常见问题** - 查看 [FAQ](./07-appendix/faq.md)
- **故障排查** - 查看 [故障排查指南](./06-development/troubleshooting.md)
- **示例代码** - 浏览 [示例库](./05-examples/)
- **GitHub Issues** - 提交问题和建议

## 🔄 文档版本

当前文档版本：v1.0  
最后更新：2024

---

**提示**：建议按照文档顺序学习，从入门指南开始，逐步掌握各项功能。每个文档都包含详细的说明和实例代码。

