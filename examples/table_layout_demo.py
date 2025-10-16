"""
表格布局参数演示

展示 Table 的新增布局参数：
- repeatRows/repeatCols: 跨页重复显示
- splitByRow: 分割方式
- hAlign/vAlign: 对齐方式
- spaceBefore/spaceAfter: 间距控制
"""

from pdf_generator.core.generator import PDFReportGenerator


def demo_repeat_rows():
    """演示 repeatRows - 跨页重复表头"""
    print("示例1: repeatRows - 跨页重复表头")
    
    # 创建足够多的数据以触发跨页
    data = [["姓名", "年龄", "部门", "职位"]]  # 表头
    for i in range(1, 51):
        data.append([f"员工{i}", str(20 + i % 30), "技术部" if i % 2 == 0 else "销售部", "工程师" if i % 2 == 0 else "销售经理"])
    
    config = {
        "title": "员工信息表（跨页重复表头）",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "员工信息表（50条记录）",
                "level": 1
            },
            {
                "type": "text",
                "content": "注意：表格跨页时，表头会在每一页重复显示"
            },
            {
                "type": "spacer",
                "height": 0.2
            },
            {
                "type": "table",
                "data": data,
                "columnWidths": [1.5, 1.0, 1.5, 2.0],
                "repeatRows": 1,  # 每页重复表头
                "spaceBefore": 0.2,
                "spaceAfter": 0.2
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_layout_01_repeat_rows.pdf")
    print("✓ 生成成功: examples/table_layout_01_repeat_rows.pdf\n")


def demo_table_alignment():
    """演示表格对齐方式"""
    print("示例2: 表格对齐方式")
    
    config = {
        "title": "表格对齐演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "表格对齐方式演示",
                "level": 1
            },
            
            # 左对齐（默认）
            {
                "type": "heading",
                "text": "1. 左对齐（LEFT）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["项目", "数值"],
                    ["A", "100"],
                    ["B", "200"]
                ],
                "columnWidths": [2.0, 1.5],
                "hAlign": "LEFT",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            },
            
            # 居中对齐
            {
                "type": "heading",
                "text": "2. 居中对齐（CENTER）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["项目", "数值"],
                    ["A", "100"],
                    ["B", "200"]
                ],
                "columnWidths": [2.0, 1.5],
                "hAlign": "CENTER",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            },
            
            # 右对齐
            {
                "type": "heading",
                "text": "3. 右对齐（RIGHT）",
                "level": 2
            },
            {
                "type": "table",
                "data": [
                    ["项目", "数值"],
                    ["A", "100"],
                    ["B", "200"]
                ],
                "columnWidths": [2.0, 1.5],
                "hAlign": "RIGHT",
                "spaceBefore": 0.1,
                "spaceAfter": 0.3
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_layout_02_alignment.pdf")
    print("✓ 生成成功: examples/table_layout_02_alignment.pdf\n")


def demo_table_spacing():
    """演示表格间距控制"""
    print("示例3: 表格间距控制")
    
    config = {
        "title": "表格间距演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "表格间距控制演示",
                "level": 1
            },
            
            {
                "type": "text",
                "content": "下面的表格设置了 spaceBefore=0.5 英寸"
            },
            {
                "type": "table",
                "data": [
                    ["产品", "价格"],
                    ["产品A", "$100"],
                    ["产品B", "$200"]
                ],
                "columnWidths": [3.0, 2.0],
                "hAlign": "CENTER",
                "spaceBefore": 0.5,  # 表格前留0.5英寸空白
                "spaceAfter": 0.1
            },
            
            {
                "type": "text",
                "content": "上面的表格设置了 spaceAfter=0.1 英寸，所以这段文字和表格的距离较近"
            },
            
            {
                "type": "spacer",
                "height": 0.5
            },
            
            {
                "type": "text",
                "content": "下面的表格设置了 spaceAfter=0.8 英寸"
            },
            {
                "type": "table",
                "data": [
                    ["服务", "费用"],
                    ["服务X", "$50"],
                    ["服务Y", "$75"]
                ],
                "columnWidths": [3.0, 2.0],
                "hAlign": "CENTER",
                "spaceBefore": 0.1,
                "spaceAfter": 0.8  # 表格后留0.8英寸空白
            },
            
            {
                "type": "text",
                "content": "这段文字和上面的表格距离较远（0.8英寸）"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_layout_03_spacing.pdf")
    print("✓ 生成成功: examples/table_layout_03_spacing.pdf\n")


def demo_comprehensive():
    """综合演示所有布局参数"""
    print("示例4: 综合布局参数演示")
    
    # 创建较多数据
    data = [["ID", "产品名称", "类别", "价格", "库存"]]
    for i in range(1, 31):
        data.append([
            str(i),
            f"产品-{i}",
            "电子产品" if i % 3 == 0 else "家居用品" if i % 3 == 1 else "服装",
            f"¥{100 + i * 10}",
            str(50 + i * 5)
        ])
    
    config = {
        "title": "综合布局演示",
        "pageSize": "A4",
        "elements": [
            {
                "type": "heading",
                "text": "产品清单（综合布局参数）",
                "level": 1
            },
            {
                "type": "text",
                "content": "本表格应用了多个布局参数：居中显示、跨页重复表头、合理间距"
            },
            {
                "type": "table",
                "data": data,
                "columnWidths": [0.6, 2.0, 1.5, 1.2, 1.0],
                "repeatRows": 1,      # 跨页重复表头
                "repeatCols": 0,      # 不重复列
                "splitByRow": True,   # 按行分割
                "hAlign": "CENTER",   # 表格居中
                "vAlign": "TOP",      # 顶部对齐
                "spaceBefore": 0.3,   # 表格前间距
                "spaceAfter": 0.3,    # 表格后间距
                "wrapColumns": [1],   # 产品名称列自动换行
                "wrapThreshold": 20
            },
            {
                "type": "text",
                "content": "表格配置说明："
            },
            {
                "type": "list",
                "items": [
                    "hAlign: CENTER - 表格在页面中居中显示",
                    "repeatRows: 1 - 跨页时每页都显示表头",
                    "spaceBefore/After: 0.3 - 表格前后留有适当空白",
                    "wrapColumns: [1] - 产品名称列支持自动换行"
                ]
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("examples/table_layout_04_comprehensive.pdf")
    print("✓ 生成成功: examples/table_layout_04_comprehensive.pdf\n")


if __name__ == "__main__":
    print("=" * 70)
    print("表格布局参数演示")
    print("=" * 70)
    print()
    
    demo_repeat_rows()
    demo_table_alignment()
    demo_table_spacing()
    demo_comprehensive()
    
    print("=" * 70)
    print("所有示例生成完成！")
    print("=" * 70)
    print("\n生成的文件：")
    print("  1. table_layout_01_repeat_rows.pdf - 跨页重复表头")
    print("  2. table_layout_02_alignment.pdf - 表格对齐方式")
    print("  3. table_layout_03_spacing.pdf - 表格间距控制")
    print("  4. table_layout_04_comprehensive.pdf - 综合布局演示")
    print()

