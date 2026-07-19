"""
31 - 页眉页脚起始页码：封面/目录不显示页眉页脚

演示 pageTemplate 中 header 和 footer 的 startPage 配置：
- 封面（第1页）和目录（第2页）不显示页眉页脚
- 页脚从第2页（目录）开始显示页码
- 页眉从第3页（正文）开始显示
- 页眉和页脚可以独立设置不同的 startPage
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "2024年度项目总结报告",
        "author": "项目管理部",
        "company": "示例科技有限公司"
    },
    "coverPage": {
        "enabled": True,
        "background": {"type": "gradient", "colorStart": "#1a1a2e", "colorEnd": "#16213e"},
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "Title",
             "position": {"x": "center", "y": 500}},
            {"type": "text", "content": "{{metadata.company}}", "style": "Heading1",
             "position": {"x": "center", "y": 400}},
            {"type": "text", "content": "编制：{{metadata.author}} | {{date}}", "style": "Normal",
             "position": {"x": "center", "y": 200}},
        ]
    },
    "toc": {
        "enabled": True,
        "autoGenerate": True,
        "title": "目  录",
        "maxLevel": 2
    },
    "pageTemplate": {
        "header": {
            "enabled": True,
            "startPage": 3,
            "height": 0.7,
            "showLine": True,
            "left": {"type": "text", "content": "{{metadata.title}}", "fontSize": 8},
            "right": {"type": "text", "content": "{{date}}", "fontSize": 8}
        },
        "footer": {
            "enabled": True,
            "startPage": 2,
            "height": 0.5,
            "showLine": True,
            "center": {
                "type": "pageNumber",
                "format": "- {page} -",
                "fontSize": 8
            }
        }
    },
    "styles": {
        "projectTable": {
            "gridColor": "#BDC3C7",
            "headerBackground": "#2980B9",
            "headerTextColor": "#FFFFFF",
            "fontSize": 9,
            "padding": 7,
            "alternateRowColor": "#EBF5FB"
        }
    },
    "dataSources": [
        {
            "name": "projects",
            "type": "inline",
            "data": [
                {"项目名称": "智能客服系统智能客服系统智能客服系统", "负责人": "张三", "状态": "已完成", "进度": "100%", "预算": 500000, "实际支出": 480000},
                {"项目名称": "数据分析平台", "负责人": "李四", "状态": "进行中", "进度": "75%", "预算": 800000, "实际支出": 620000},
                {"项目名称": "移动端APP", "负责人": "王五", "状态": "进行中", "进度": "60%", "预算": 600000, "实际支出": 350000},
                {"项目名称": "云基础设施", "负责人": "赵六", "状态": "已完成", "进度": "100%", "预算": 1200000, "实际支出": 1150000},
                {"项目名称": "安全审计系统", "负责人": "钱七", "状态": "规划中", "进度": "20%", "预算": 300000, "实际支出": 50000},
            ]
        }
    ],
    "elements": [
        {"type": "heading", "text": "一、项目总览", "level": 1},
        {"type": "text", "content": "本报告总结了2024年度公司各核心项目的执行情况。"},
        {"type": "spacer", "height": 0.15},
        {"type": "text", "content": "📌 提示：翻到封面页（第1页）和目录页（第2页），观察是否没有页眉页脚。"},
        {"type": "text", "content": "📌 从本页（第3页）开始，页眉页脚才出现。页脚从目录页（第2页）就开始了。"},
        {"type": "spacer", "height": 0.2},
        {"type": "table", "dataSource": "projects", "style": "projectTable",
         "columnWidths": [1.0, 1.0, 1.0, 1.0, 1.0, 1.2]},
        {"type": "pagebreak"},

        {"type": "heading", "text": "二、项目进度详情", "level": 1},
        {"type": "text", "content": "2.1 已完成项目"},
        {"type": "text", "content": "智能客服系统和云基础设施升级项目已按计划完成，交付质量获得客户好评。"},
        {"type": "text", "content": "2.2 进行中项目"},
        {"type": "text", "content": "数据分析平台已完成核心模块开发，预计下季度进入测试阶段。移动端APP开发进度60%，预计年底前完成第一版。"},
        {"type": "text", "content": "2.3 规划中项目"},
        {"type": "text", "content": "安全审计系统已完成需求调研，正在进行技术方案设计。"},
        {"type": "pagebreak"},

        {"type": "heading", "text": "三、预算与资源分析", "level": 1},
        {"type": "text", "content": "全年项目预算总计340万元，实际支出265万元，预算执行率78%。"},
        {"type": "text", "content": "云基础设施项目预算最大（120万），实际支出控制良好（115万）。"},
        {"type": "text", "content": "建议下一年度优化资源配置，加大对数据分析平台的投入。"},
        {"type": "pagebreak"},

        {"type": "heading", "text": "四、总结与展望", "level": 1},
        {"type": "text", "content": "2024年度项目执行情况总体良好，重点项目按时交付率90%。"},
        {"type": "text", "content": "下一年度计划：引入AI技术提升项目管理效率，建立标准化流程体系。"},
        {"type": "spacer", "height": 0.3},
        {"type": "text", "content": "报告生成日期：{{date}}"},
        {"type": "text", "content": "本页（约第6页）仍然有页眉页脚，说明 startPage 之后的页面都会正常显示。"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/31_header_footer_start_page.pdf")
print("✅ 已生成: examples/output/31_header_footer_start_page.pdf")
print()
print("📋 验证要点：")
print("   - 第1页（封面）：无页眉页脚")
print("   - 第2页（目录）：无页眉，有页脚（页码）")
print("   - 第3页及之后（正文）：有页眉有页脚")
