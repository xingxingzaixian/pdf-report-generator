# 示例

PDF Report Generator 提供了丰富的示例代码，帮助你快速上手。

## 示例分类

### [基础示例](./basics.md)

从零开始，学习基本的 PDF 生成：

- `01_hello_pdf.py` - 最简单的 Hello PDF
- `02_text_styles.py` - 文本样式
- `03_simple_table.py` - 简单表格
- `11_image.py` - 插入图片
- `16_page_break.py` - 分页控制

### [数据源示例](./data-sources.md)

学习如何从不同数据源获取数据：

- `04_data_csv.py` - CSV 数据源
- `05_data_json.py` - JSON 数据源
- `06_data_excel.py` - Excel 数据源
- `07_data_dataframe.py` - DataFrame 数据源
- `08_data_api.py` - API 数据源

### [图表示例](./charts.md)

生成各种类型的图表：

- `09_chart_bar.py` - 柱状图
- `10_chart_line_pie.py` - 折线图和饼图

### 高级功能示例

使用高级排版功能：

- `12_header_footer.py` - 页眉页脚
- `13_page_number.py` - 页码
- `14_toc.py` - 自动目录
- `15_cover_page.py` - 封面页
- `17_table_merge.py` - 表格合并

### [综合示例](./comprehensive.md)

完整的报告案例：

- `25_comprehensive_sales.py` - 销售报告
- `26_comprehensive_financial.py` - 财务报告
- `27_comprehensive_project.py` - 项目报告

### [Pipeline 示例](./pipeline.md)

数据处理管道：

- `21_pipeline_filter.py` - 数据过滤
- `22_pipeline_transform.py` - 数据转换
- `23_pipeline_aggregate.py` - 数据聚合
- `24_pipeline_full_workflow.py` - 完整工作流

## 运行示例

```bash
# 运行单个示例
python examples/01_hello_pdf.py

# 运行所有示例
cd examples
bash run_all.sh
```

## 输出位置

所有示例的输出文件保存在 `examples/output/` 目录下。
