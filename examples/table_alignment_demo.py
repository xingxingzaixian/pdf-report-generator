"""
表格单元格对齐方式演示

展示如何控制单元格内文本的对齐方式：
1. 通过样式设置全局对齐方式
2. 通过 cellAlignments 设置特定单元格/列/行的对齐方式
"""

from pdf_generator.core.generator import PDFReportGenerator


def demo_style_alignment():
    """通过样式设置全局对齐方式"""
    print("示例1: 通过样式设置全局对齐")
    
    config = {
        "title": "表格对齐方式演示",
        "pageSize": "A4",
        "styles": {
            # 自定义表格样式：左对齐 + 顶部对齐
            "left_top_style": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#4472C4",
                "headerTextColor": "#FFFFFF",
                "fontSize": 9,
                "padding": 8,
                "alignment": "LEFT",      # 水平左对齐
                "valignment": "TOP"       # 垂直顶部对齐
            },
            # 居中对齐 + 中间对齐
            "center_middle_style": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#70AD47",
                "headerTextColor": "#FFFFFF",
                "fontSize": 9,
                "padding": 8,
                "alignment": "CENTER",    # 水平居中
                "valignment": "MIDDLE"    # 垂直居中（默认）
            },
            # 右对齐 + 底部对齐
            "right_bottom_style": {
                "gridColor": "#CCCCCC",
                "headerBackground": "#FFC000",
                "headerTextColor": "#000000",
                "fontSize": 9,
                "padding": 8,
                "alignment": "RIGHT",     # 水平右对齐
                "valignment": "BOTTOM"    # 垂直底部对齐
            }
        },
        "elements": [
            {
                "type": "heading",
                "text": "1. 左对齐 + 顶部对齐（LEFT + TOP）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["姓名", "年龄", "部门"],
                    ["张三", "28", "技术部"],
                    ["李四", "32", "销售部"],
                    ["王五", "25", "市场部"]
                ],
                "columnWidths": [2.0, 1.5, 2.0],
                "rowHeights": [0.4, 0.6, 0.6, 0.6],  # 增加行高以便看到垂直对齐效果
                "style": "left_top_style",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            },
            
            {
                "type": "heading",
                "text": "2. 居中对齐 + 中间对齐（CENTER + MIDDLE）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["产品", "价格", "库存"],
                    ["产品A", "¥1,200", "50"],
                    ["产品B", "¥800", "120"],
                    ["产品C", "¥1,500", "30"]
                ],
                "columnWidths": [2.0, 1.5, 2.0],
                "rowHeights": [0.4, 0.6, 0.6, 0.6],
                "style": "center_middle_style",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            },
            
            {
                "type": "heading",
                "text": "3. 右对齐 + 底部对齐（RIGHT + BOTTOM）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["项目", "金额", "状态"],
                    ["项目X", "$5,000", "进行中"],
                    ["项目Y", "$8,000", "已完成"],
                    ["项目Z", "$3,500", "计划中"]
                ],
                "columnWidths": [2.0, 1.5, 2.0],
                "rowHeights": [0.4, 0.6, 0.6, 0.6],
                "style": "right_bottom_style",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_align_01_style.pdf")
    print("✓ 生成成功: examples/table_align_01_style.pdf\n")


def demo_cell_alignments():
    """通过 cellAlignments 设置特定单元格的对齐方式"""
    print("示例2: 设置特定单元格的对齐方式")
    
    config = {
        "title": "单元格对齐演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "财务报表（混合对齐方式）",
                "level": 1
            },
            {
                "type": "text",
                "content": "说明：项目名称左对齐，金额右对齐，状态居中对齐"
            },
            {
                "type": "spacer",
                "height": 0.2
            },
            {
                "type": "table",
                "data": [
                    ["项目名称", "Q1", "Q2", "Q3", "Q4", "总计", "状态"],
                    ["营业收入", "50,000", "55,000", "60,000", "65,000", "230,000", "良好"],
                    ["营业成本", "30,000", "32,000", "35,000", "38,000", "135,000", "正常"],
                    ["毛利润", "20,000", "23,000", "25,000", "27,000", "95,000", "优秀"],
                    ["运营费用", "10,000", "11,000", "12,000", "13,000", "46,000", "正常"],
                    ["净利润", "10,000", "12,000", "13,000", "14,000", "49,000", "优秀"]
                ],
                "columnWidths": [1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8],
                "rowHeights": [0.4, 0.5, 0.5, 0.5, 0.5, 0.5],
                "cellAlignments": [
                    # 第一列（项目名称）左对齐
                    {"range": [0, 0, 5, 0], "align": "LEFT", "valign": "MIDDLE"},
                    # 金额列（Q1-Q4、总计）右对齐
                    {"range": [0, 1, 5, 5], "align": "RIGHT", "valign": "MIDDLE"},
                    # 状态列居中对齐
                    {"range": [0, 6, 5, 6], "align": "CENTER", "valign": "MIDDLE"}
                ],
                "hAlign": "CENTER",
                "spaceBefore": 0.2
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_align_02_cells.pdf")
    print("✓ 生成成功: examples/table_align_02_cells.pdf\n")


def demo_column_alignments():
    """演示按列设置对齐方式"""
    print("示例3: 按列设置对齐方式")
    
    config = {
        "title": "列对齐演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "产品价格表（按列对齐）",
                "level": 1
            },
            {
                "type": "text",
                "content": "第1列左对齐，第2-3列居中对齐，第4-5列右对齐"
            },
            {
                "type": "spacer",
                "height": 0.2
            },
            {
                "type": "table",
                "data": [
                    ["产品名称", "类别", "规格", "单价", "库存"],
                    ["MacBook Pro", "电脑", "16英寸", "¥18,999", "25"],
                    ["iPad Air", "平板", "10.9英寸", "¥4,799", "50"],
                    ["iPhone 15", "手机", "256GB", "¥6,999", "100"],
                    ["AirPods Pro", "配件", "无线", "¥1,899", "200"],
                    ["Apple Watch", "穿戴", "GPS", "¥3,199", "80"]
                ],
                "columnWidths": [2.0, 1.2, 1.5, 1.5, 1.0],
                "cellAlignments": [
                    # 第1列（产品名称）：左对齐
                    {"range": [0, 0, 5, 0], "align": "LEFT"},
                    # 第2-3列（类别、规格）：居中对齐
                    {"range": [0, 1, 5, 2], "align": "CENTER"},
                    # 第4-5列（单价、库存）：右对齐
                    {"range": [0, 3, 5, 4], "align": "RIGHT"},
                    # 所有单元格顶部对齐
                    {"range": [0, 0, 5, 4], "valign": "TOP"}
                ],
                "hAlign": "CENTER",
                "spaceBefore": 0.2
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_align_03_columns.pdf")
    print("✓ 生成成功: examples/table_align_03_columns.pdf\n")


def demo_complex_alignment():
    """演示复杂的对齐组合"""
    print("示例4: 复杂对齐组合")
    
    config = {
        "title": "复杂对齐演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "课程成绩表（复杂对齐）",
                "level": 1
            },
            {
                "type": "spacer",
                "height": 0.2
            },
            {
                "type": "table",
                "data": [
                    ["姓名", "语文", "数学", "英语", "总分", "等级"],
                    ["张三", "90", "85", "88", "263", "A"],
                    ["李四", "88", "92", "85", "265", "A"],
                    ["王五", "85", "88", "90", "263", "A"],
                    ["赵六", "92", "95", "93", "280", "A+"],
                    ["平均分", "88.75", "90.0", "89.0", "267.75", "-"]
                ],
                "columnWidths": [1.5, 1.0, 1.0, 1.0, 1.2, 0.8],
                "rowHeights": [0.4, 0.5, 0.5, 0.5, 0.5, 0.5],
                "cellAlignments": [
                    # 表头行：全部居中
                    {"range": [0, 0, 0, 5], "align": "CENTER", "valign": "MIDDLE"},
                    # 姓名列：左对齐
                    {"range": [1, 0, 5, 0], "align": "LEFT", "valign": "MIDDLE"},
                    # 分数列：居中对齐
                    {"range": [1, 1, 4, 3], "align": "CENTER", "valign": "MIDDLE"},
                    # 总分列：右对齐加粗（通过增加行高突出）
                    {"range": [1, 4, 4, 4], "align": "RIGHT", "valign": "MIDDLE"},
                    # 等级列：居中对齐
                    {"range": [1, 5, 4, 5], "align": "CENTER", "valign": "MIDDLE"},
                    # 最后一行（平均分）：整行右对齐
                    {"range": [5, 1, 5, 4], "align": "RIGHT", "valign": "MIDDLE"},
                    # 平均分标签：左对齐
                    {"range": [5, 0, 5, 0], "align": "LEFT", "valign": "MIDDLE"}
                ],
                "hAlign": "CENTER",
                "spaceBefore": 0.2
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_align_04_complex.pdf")
    print("✓ 生成成功: examples/table_align_04_complex.pdf\n")


if __name__ == "__main__":
    print("=" * 70)
    print("表格对齐方式演示")
    print("=" * 70)
    print()
    
    demo_style_alignment()
    demo_cell_alignments()
    demo_column_alignments()
    demo_complex_alignment()
    
    print("=" * 70)
    print("所有示例生成完成！")
    print("=" * 70)
    print("\n生成的文件：")
    print("  1. table_align_01_style.pdf - 通过样式设置全局对齐")
    print("  2. table_align_02_cells.pdf - 设置特定单元格对齐")
    print("  3. table_align_03_columns.pdf - 按列设置对齐")
    print("  4. table_align_04_complex.pdf - 复杂对齐组合")
    print()

