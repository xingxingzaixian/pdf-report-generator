"""
表格单元格合并示例

演示如何创建包含合并单元格的复杂表格
"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pdf_generator import PDFReportGenerator

print("=" * 70)
print("表格单元格合并示例")
print("=" * 70)
print()

# 示例1: 简单的标题行合并
def example1_simple_merge():
    """简单的表头合并"""
    print("示例1: 表头合并")
    
    config = {
        "metadata": {
            "title": "单元格合并示例 - 表头合并",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 18,
                "alignment": "center",
                "bold": True,
                "spaceAfter": 20
            },
            "mergeTable": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#4472C4",
                "headerTextColor": "#FFFFFF",
                "fontSize": 10,
                "padding": 8
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "text",
                "content": "以下表格展示了跨列合并的表头："
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "table",
                "data": [
                    ["销售统计", "", "", ""],  # 第一行：大标题（将被合并）
                    ["产品", "Q1", "Q2", "Q3"],  # 第二行：子表头
                    ["笔记本", "100", "120", "150"],
                    ["台式机", "80", "90", "95"],
                    ["平板", "150", "180", "200"]
                ],
                "style": "mergeTable",
                "columnWidths": [2, 1.2, 1.2, 1.2],
                "mergedCells": [
                    [0, 0, 0, 3]  # 合并第0行，从第0列到第3列（销售统计）
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("table_merge_01_simple.pdf")
    print("✓ 生成成功: table_merge_01_simple.pdf\n")


# 示例2: 复杂的多区域合并
def example2_complex_merge():
    """复杂的多区域合并"""
    print("示例2: 复杂表格合并")
    
    config = {
        "metadata": {
            "title": "复杂表格合并示例",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 18,
                "alignment": "center",
                "bold": True,
                "spaceAfter": 20
            },
            "complexTable": {
                "gridColor": "#999999",
                "headerBackground": "#2E75B6",
                "headerTextColor": "#FFFFFF",
                "fontSize": 9,
                "padding": 6
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "text",
                "content": "以下表格展示了多种单元格合并方式："
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "table",
                "data": [
                    ["项目进度表", "", "", "", ""],  # 标题行
                    ["阶段", "任务", "负责人", "开始日期", "结束日期"],  # 表头
                    ["需求分析", "需求调研", "张三", "2024-01", "2024-02"],
                    ["", "需求文档", "张三", "2024-02", "2024-03"],  # 阶段列将被合并
                    ["设计阶段", "UI设计", "李四", "2024-03", "2024-04"],
                    ["", "架构设计", "王五", "2024-03", "2024-04"],
                    ["", "数据库设计", "王五", "2024-04", "2024-05"],
                    ["开发阶段", "前端开发", "赵六", "2024-05", "2024-07"],
                    ["", "后端开发", "钱七", "2024-05", "2024-07"],
                    ["", "接口联调", "全员", "2024-07", "2024-08"]
                ],
                "style": "complexTable",
                "columnWidths": [1.5, 1.8, 1.2, 1.5, 1.5],
                "mergedCells": [
                    [0, 0, 0, 4],     # 标题行：合并整行
                    [2, 0, 3, 0],     # 需求分析阶段：合并2行
                    [4, 0, 6, 0],     # 设计阶段：合并3行
                    [7, 0, 9, 0]      # 开发阶段：合并3行
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("table_merge_02_complex.pdf")
    print("✓ 生成成功: table_merge_02_complex.pdf\n")


# 示例3: 财务报表样式
def example3_financial_report():
    """财务报表样式的合并表格"""
    print("示例3: 财务报表")
    
    config = {
        "metadata": {
            "title": "2024年第一季度财务报表",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 18,
                "alignment": "center",
                "bold": True,
                "spaceAfter": 20
            },
            "financialTable": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#1F4788",
                "headerTextColor": "#FFFFFF",
                "fontSize": 10,
                "padding": 8
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "table",
                "data": [
                    ["财务指标", "1月", "2月", "3月", "季度总计"],
                    ["收入", "", "", "", ""],  # 收入大类
                    ["  产品销售", "500", "550", "600", "1650"],
                    ["  服务收入", "200", "220", "250", "670"],
                    ["  其他收入", "50", "60", "70", "180"],
                    ["收入小计", "750", "830", "920", "2500"],  # 小计行
                    ["支出", "", "", "", ""],  # 支出大类
                    ["  人力成本", "300", "300", "320", "920"],
                    ["  运营成本", "150", "160", "170", "480"],
                    ["  营销费用", "100", "120", "130", "350"],
                    ["支出小计", "550", "580", "620", "1750"],  # 小计行
                    ["净利润", "200", "250", "300", "750"]  # 总计行
                ],
                "style": "financialTable",
                "columnWidths": [2, 1.2, 1.2, 1.2, 1.5],
                "mergedCells": [
                    [1, 1, 1, 4],     # 收入：合并数据列
                    [6, 1, 6, 4]      # 支出：合并数据列
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("table_merge_03_financial.pdf")
    print("✓ 生成成功: table_merge_03_financial.pdf\n")


# 示例4: 课程表样式
def example4_schedule():
    """课程表样式"""
    print("示例4: 课程表")
    
    config = {
        "metadata": {
            "title": "课程表",
            "pageSize": "A4",
            "orientation": "landscape"  # 横向布局更适合课程表
        },
        "styles": {
            "title": {
                "fontSize": 20,
                "alignment": "center",
                "bold": True,
                "spaceAfter": 20
            },
            "scheduleTable": {
                "gridColor": "#666666",
                "headerBackground": "#3498DB",
                "headerTextColor": "#FFFFFF",
                "fontSize": 9,
                "padding": 5
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "table",
                "data": [
                    ["时间", "周一", "周二", "周三", "周四", "周五"],
                    ["08:00-09:30", "数学", "语文", "英语", "物理", "化学"],
                    ["10:00-11:30", "语文", "数学", "体育", "英语", "生物"],
                    ["14:00-15:30", "物理", "化学", "数学", "语文", "英语"],
                    ["16:00-17:30", "自习", "自习", "自习", "自习", "班会"]
                ],
                "style": "scheduleTable",
                "columnWidths": [1.5, 1.8, 1.8, 1.8, 1.8, 1.8],
                "mergedCells": []  # 这个例子不需要合并，展示标准表格
            },
            {
                "type": "spacer",
                "height": 0.5
            },
            {
                "type": "text",
                "content": "特殊课程安排（跨时段）："
            },
            {
                "type": "spacer",
                "height": 0.2
            },
            {
                "type": "table",
                "data": [
                    ["时间", "周一", "周二", "周三", "周四", "周五"],
                    ["08:00-09:30", "数学", "实验课", "英语", "物理", "化学"],
                    ["10:00-11:30", "语文", "", "体育", "英语", "生物"],  # 实验课占2个时段
                    ["14:00-15:30", "物理", "化学", "数学", "项目实践", "英语"],
                    ["16:00-17:30", "自习", "自习", "自习", "", "班会"]  # 项目实践占2个时段
                ],
                "style": "scheduleTable",
                "columnWidths": [1.5, 1.8, 1.8, 1.8, 1.8, 1.8],
                "mergedCells": [
                    [1, 2, 2, 2],     # 周二实验课：跨2个时段
                    [3, 4, 4, 4]      # 周四项目实践：跨2个时段
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("table_merge_04_schedule.pdf")
    print("✓ 生成成功: table_merge_04_schedule.pdf\n")


# 示例5: 使用数据源的合并表格
def example5_datasource_merge():
    """从数据源创建带合并的表格"""
    print("示例5: 数据源 + 单元格合并")
    
    import pandas as pd
    
    # 准备数据
    data = pd.DataFrame({
        "类别": ["收入", "", "", "支出", "", ""],
        "项目": ["产品销售", "服务收入", "小计", "人力成本", "运营成本", "小计"],
        "金额": [1000, 500, 1500, 800, 300, 1100],
        "占比": ["66.7%", "33.3%", "100%", "72.7%", "27.3%", "100%"]
    })
    
    config = {
        "metadata": {
            "title": "收支明细表（带合并）",
            "pageSize": "A4"
        },
        "styles": {
            "title": {
                "fontSize": 18,
                "alignment": "center",
                "bold": True,
                "spaceAfter": 20
            },
            "dataTable": {
                "gridColor": "#AAAAAA",
                "headerBackground": "#2C3E50",
                "headerTextColor": "#FFFFFF",
                "fontSize": 10
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "{{metadata.title}}",
                "style": "title"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "table",
                "dataSource": "financial",
                "style": "dataTable",
                "columnWidths": [1.5, 2, 1.5, 1.5],
                "mergedCells": [
                    [1, 0, 3, 0],     # 合并"收入"类别（3行）
                    [4, 0, 6, 0]      # 合并"支出"类别（3行）
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.add_data_source("financial", data)
    generator.save("table_merge_05_datasource.pdf")
    print("✓ 生成成功: table_merge_05_datasource.pdf\n")


if __name__ == "__main__":
    print("开始生成表格合并示例...\n")
    
    example1_simple_merge()
    example2_complex_merge()
    example3_financial_report()
    example4_schedule()
    example5_datasource_merge()
    
    print("=" * 70)
    print("所有示例生成完成！")
    print("=" * 70)
    print("\n生成的文件：")
    print("  1. table_merge_01_simple.pdf - 简单表头合并")
    print("  2. table_merge_02_complex.pdf - 复杂多区域合并")
    print("  3. table_merge_03_financial.pdf - 财务报表")
    print("  4. table_merge_04_schedule.pdf - 课程表")
    print("  5. table_merge_05_datasource.pdf - 数据源+合并")
    print()

