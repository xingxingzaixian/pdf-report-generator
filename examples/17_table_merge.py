"""
17 - 单元格合并：跨行/跨列/标题行/财务报表

演示 mergedCells 配置的多种合并方式。
每个合并项格式: [startRow, startCol, endRow, endCol]
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "单元格合并示例"},
    "styles": {
        "mt": {
            "gridColor": "#999999", "headerBackground": "#2E75B6",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 6
        }
    },
    "elements": [
        {"type": "text", "content": "{{metadata.title}}", "style": "Title"},
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "1. 跨列合并标题行 [0,0,0,3]", "style": "Heading2"},
        {
            "type": "table",
            "data": [
                ["销售统计表", "", "", ""],
                ["产品", "Q1", "Q2", "Q3"],
                ["笔记本", "100", "120", "150"],
                ["台式机", "80", "90", "95"],
                ["平板", "150", "180", "200"],
            ],
            "style": "mt", "columnWidths": [2, 1.2, 1.2, 1.2],
            "mergedCells": [[0, 0, 0, 3]]
        },
        {"type": "pagebreak"},

        {"type": "text", "content": "2. 跨行合并阶段列", "style": "Heading2"},
        {
            "type": "table",
            "data": [
                ["项目进度表", "", "", "", ""],
                ["阶段", "任务", "负责人", "开始", "结束"],
                ["需求分析", "需求调研", "张三", "1月", "2月"],
                ["", "需求文档", "张三", "2月", "3月"],
                ["设计阶段", "UI设计", "李四", "3月", "4月"],
                ["", "架构设计", "王五", "3月", "4月"],
                ["", "数据库", "王五", "4月", "5月"],
            ],
            "style": "mt", "columnWidths": [1.5, 1.8, 1.2, 1.2, 1.2],
            "mergedCells": [
                [0, 0, 0, 4], [2, 0, 3, 0], [4, 0, 6, 0],
            ]
        },
        {"type": "pagebreak"},

        {"type": "text", "content": "3. 财务报表 - 收入/支出大类标签", "style": "Heading2"},
        {
            "type": "table",
            "data": [
                ["财务指标", "1月", "2月", "3月", "合计"],
                ["收入", "", "", "", ""],
                ["  产品销售", "500", "550", "600", "1650"],
                ["  服务收入", "200", "220", "250", "670"],
                ["  小计", "700", "770", "850", "2320"],
                ["支出", "", "", "", ""],
                ["  人力成本", "300", "300", "320", "920"],
                ["  运营成本", "150", "160", "170", "480"],
                ["  小计", "450", "460", "490", "1400"],
                ["净利润", "250", "310", "360", "920"],
            ],
            "style": "mt", "columnWidths": [2, 1.2, 1.2, 1.2, 1.2],
            "mergedCells": [[1, 1, 1, 4], [5, 1, 5, 4]]
        },
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/17_table_merge.pdf")
print("✅ 已生成: examples/output/17_table_merge.pdf")
