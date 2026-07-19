"""
27 - 综合报告：项目报告（图片+表格+目录+封面+页脚）

使用 config dataSources inline + 合并表格，无需 add_data_source。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {
        "title": "X项目进度报告",
        "author": "项目管理部",
        "company": "示例科技有限公司"
    },
    "coverPage": {
        "enabled": True,
        "background": {"type": "gradient", "colorStart": "#0F2027", "colorEnd": "#203A43"},
        "elements": [
            {"type": "text", "content": "{{metadata.title}}", "style": "Title",
             "position": {"x": "center", "y": 520}},
            {"type": "text", "content": "项目阶段汇报", "style": "Heading1",
             "position": {"x": "center", "y": 430}},
            {"type": "text", "content": "{{metadata.company}}", "style": "Normal",
             "position": {"x": "center", "y": 220}},
            {"type": "text", "content": "报告日期：{{date}}", "style": "Normal",
             "position": {"x": "center", "y": 170}},
        ]
    },
    "toc": {"enabled": True, "autoGenerate": True, "title": "目  录", "maxLevel": 2},
    "pageTemplate": {
        "header": {
            "enabled": True, "height": 0.7, "showLine": True,
            "left": {"type": "text", "content": "{{metadata.title}} - 内部文档"},
            "right": {"type": "text", "content": "{{date}}"}
        },
        "footer": {
            "enabled": True, "height": 0.5, "showLine": True,
            "center": {"type": "pageNumber", "format": "第{page}页"},
            "right": {"type": "text", "content": "保密", "color": "#FF0000", "fontSize": 8}
        }
    },
    "styles": {
        "progressTable": {
            "gridColor": "#BDC3C7", "headerBackground": "#2C3E50",
            "headerTextColor": "#FFFFFF", "fontSize": 9, "padding": 6
        }
    },
    "dataSources": [
        {
            "name": "progress",
            "type": "inline",
            "data": [
                {"阶段": "需求分析", "任务": "需求调研", "负责人": "张三", "开始": "1月", "结束": "2月", "状态": "✅ 完成"},
                {"阶段": "需求分析", "任务": "需求文档", "负责人": "张三", "开始": "2月", "结束": "2月", "状态": "✅ 完成"},
                {"阶段": "UI设计", "任务": "界面设计", "负责人": "李四", "开始": "3月", "结束": "4月", "状态": "✅ 完成"},
                {"阶段": "架构设计", "任务": "技术方案", "负责人": "王五", "开始": "3月", "结束": "4月", "状态": "✅ 完成"},
                {"阶段": "前端开发", "任务": "页面开发", "负责人": "赵六", "开始": "4月", "结束": "6月", "状态": "🔄 进行中"},
                {"阶段": "前端开发", "任务": "组件开发", "负责人": "赵六", "开始": "4月", "结束": "5月", "状态": "✅ 完成"},
                {"阶段": "后端开发", "任务": "API开发", "负责人": "钱七", "开始": "4月", "结束": "6月", "状态": "🔄 进行中"},
                {"阶段": "测试", "任务": "单元测试", "负责人": "孙八", "开始": "6月", "结束": "7月", "状态": "📋 未开始"},
                {"阶段": "测试", "任务": "集成测试", "负责人": "孙八", "开始": "7月", "结束": "7月", "状态": "📋 未开始"},
                {"阶段": "上线", "任务": "生产部署", "负责人": "全员", "开始": "8月", "结束": "8月", "状态": "📋 未开始"},
            ]
        }
    ],
    "elements": [
        {"type": "heading", "text": "一、项目概述", "level": 1},
        {"type": "text", "content": "X项目是公司2024年度重点研发项目，打造新一代智能分析平台。"},
        {"type": "text", "content": "项目周期：2024年1月 - 2024年8月 | 团队：10人"},
        {"type": "spacer", "height": 0.3},

        {"type": "heading", "text": "二、系统架构", "level": 1},
        {
            "type": "image", "path": "examples/demo.png",
            "width": 450, "height": 225,
            "alignment": "center", "keepAspectRatio": True
        },
        {"type": "text", "content": "图1: 系统架构概览"},
        {"type": "pagebreak"},

        {"type": "heading", "text": "三、项目进度", "level": 1},
        {"type": "text", "content": "3.1 任务进度明细"},
        {
            "type": "table", "dataSource": "progress", "style": "progressTable",
            "columnWidths": [1.2, 1.5, 1.0, 1.0, 1.0, 1.0],
            "mergedCells": [
                [1, 0, 2, 0],  # 需求分析合并2行
                [5, 0, 6, 0],  # 前端开发合并2行
                [8, 0, 9, 0],  # 测试合并2行
            ]
        },
        {"type": "pagebreak"},

        {"type": "heading", "text": "四、里程碑", "level": 1},
        {"type": "table", "data": [
            ["里程碑", "计划日期", "实际日期", "状态"],
            ["需求评审通过", "2024年2月", "2024年2月", "✅ 完成"],
            ["设计评审通过", "2024年4月", "2024年4月", "✅ 完成"],
            ["Alpha版本发布", "2024年6月", "2024年6月", "✅ 完成"],
            ["Beta版本发布", "2024年7月", "—", "🔄 计划中"],
            ["正式上线", "2024年8月", "—", "📋 待定"],
        ], "style": "progressTable", "columnWidths": [2.5, 1.5, 1.5, 1.2]},
        {"type": "pagebreak"},

        {"type": "heading", "text": "五、风险与问题", "level": 1},
        {"type": "text", "content": "1. 后端API开发进度略有延迟，可能影响联调时间。"},
        {"type": "text", "content": "2. 测试资源不足，需要协调增加测试人员。"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "应对措施：", "style": "Heading2"},
        {"type": "text", "content": "• 增加后端开发人力投入"},
        {"type": "text", "content": "• 提前启动部分模块的测试工作"},
        {"type": "text", "content": "• 与产品确认缩减非核心功能范围"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/27_comprehensive_project.pdf")
print("✅ 已生成: examples/output/27_comprehensive_project.pdf")
