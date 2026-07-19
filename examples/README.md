# PDF Report Generator 示例

按从简到难的顺序排列，每个示例都可以独立运行。

## 快速开始

```bash
# 安装依赖
pip install pdf-report-generator

# 运行第一个示例
python examples/01_hello_pdf.py
```

所有生成的 PDF 文件保存在 `examples/output/` 目录下。

---

## 示例索引

### L1 - 快速入门
| 文件 | 说明 |
|------|------|
| `01_hello_pdf.py` | 5行代码生成第一个 PDF |
| `02_text_styles.py` | 文本元素 + 预设/自定义样式 |
| `03_simple_table.py` | 内嵌数据表格 + 列宽/行高 |

### L2 - 数据源
| 文件 | 说明 |
|------|------|
| `04_data_csv.py` | CSV 文件作为数据源 |
| `05_data_json.py` | JSON 文件作为数据源 |
| `06_data_excel.py` | Excel 文件作为数据源 |
| `07_data_dataframe.py` | 编程方式注入 DataFrame |
| `08_data_api.py` | HTTP API 数据源 |

### L3 - 可视化
| 文件 | 说明 |
|------|------|
| `09_chart_bar.py` | 柱状图（单/多Y轴、堆叠） |
| `10_chart_line_pie.py` | 折线图 + 饼图 |
| `11_image.py` | 图片插入（对齐、比例、尺寸） |

### L4 - 文档结构
| 文件 | 说明 |
|------|------|
| `12_header_footer.py` | 页眉页脚（三栏布局、变量） |
| `13_page_number.py` | 页码格式（阿拉伯/罗马/中文） |
| `14_toc.py` | 自动目录（多级标题、自动页码） |
| `15_cover_page.py` | 封面页（纯色/渐变、文本定位） |
| `16_page_break.py` | 分页控制 + 页面方向切换 |

### L5 - 高级表格
| 文件 | 说明 |
|------|------|
| `17_table_merge.py` | 单元格合并（跨行/跨列/标题行） |
| `18_table_alignment.py` | 单元格对齐（全局样式/精确控制） |
| `19_table_layout.py` | 表格布局（跨页表头/间距/换行） |
| `20_table_style_variants.py` | 多种表格样式变体 |

### L6 - Pipeline 管道
| 文件 | 说明 |
|------|------|
| `21_pipeline_filter.py` | 管道：filter 过滤 + sort 排序 |
| `22_pipeline_transform.py` | 管道：compute/rename/select |
| `23_pipeline_aggregate.py` | 管道：group 分组聚合 + concat |
| `24_pipeline_full_workflow.py` | 管道：完整多步骤链式处理 |

### L7 - 综合报告
| 文件 | 说明 |
|------|------|
| `25_comprehensive_sales.py` | 综合：销售报告（封面+目录+图表） |
| `26_comprehensive_financial.py` | 综合：财务报告（合并表格+管道） |
| `27_comprehensive_project.py` | 综合：项目报告（图片+多表格） |

### 专题 - 字体与 API
| 文件 | 说明 |
|------|------|
| `28_font_auto_detect.py` | 字体：自动检测 + 指定目录 |
| `29_font_custom_register.py` | 字体：手动注册 + 多字体混用 |
| `30_api_client.py` | API：客户端调用示例 |
