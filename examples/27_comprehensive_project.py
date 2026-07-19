"""
27 - 综合报告：项目报告（图片+表格+目录+封面+页脚）

演示项目进度报告，包含：
- 封面页 + 自动目录
- 项目图片展示
- 进度表格 + 合并单元格
- 里程碑时间线
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from pdf_generator import PDFReportGenerator

# 项目进度数据
progress = pd.DataFrame({
    "阶段": ["需求分析", "需求分析", "UI设计", "架构设计", "前端开发", "前端开发", "后端开发", "测试", "测试", "上线"],
    "任务": ["需求调研", "需求文档", "界面设计", "技术方案", "页面开发", "组件开发", "API开发", "单元测试", "集成测试", "生产部署"],
    "负责人": ["张三", "张三", "李四", "王五", "赵六", "赵六", "钱七", "孙八", "孙八", "全员"],
    "开始": ["1月", "2月", "3月", "3月", "4月", "4月", "4月", "6月", "7月", "8月"],
    "结束": ["2月", "2月", "4月", "4月", "6月", "5月", "6月", "7月", "7月", "8月"],
    "状态": ["完成", "完成", "完成", "完成", "进行中", "完成", "进行中", "未开始", "未开始", "未开始"],
})

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
    "elements": [
        {"type": "heading", "text": "一、项目概述", "level": 1},
        {"type": "text", "content": "X项目是公司2024年度重点研发项目，旨在打造新一代智能分析平台。"},
        {"type": "text", "content": "项目周期：2024年1月 - 2024年8月"},
        {"type": "text", "content": "项目团队：10人（含产品经理1人、设计师1人、开发6人、测试2人）"},
        {"type": "spacer", "height": 0.3},

        # 插入项目架构图（如果存在）
        {"type": "heading", "text": "二、系统架构", "level": 1},
        {"type": "text", "content": "以下为系统架构示意图："},
        {
            "type": "image",
            "path": "examples/demo.png",
            "width": 450, "height": 225,
            "alignment": "center", "keepAspectRatio": True
        },
        {"type": "text", "content": "图1: 系统架构概览", "style": "Normal"},
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
        {"type": "spacer", "height": 0.3},

        {"type": "text", "content": "3.2 完成情况统计"},
        {"type": "text", "content": f"• 已完成任务: 6/10 (60%)"},
        {"type": "text", "content": f"• 进行中任务: 2/10 (20%)"},
        {"type": "text", "content": f"• 未开始任务: 2/10 (20%)"},
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
        {"type": "text", "content": "当前项目面临的主要风险："},
        {"type": "text", "content": "1. 后端API开发进度略有延迟，可能影响联调时间。"},
        {"type": "text", "content": "2. 测试资源不足，需要协调增加测试人员。"},
        {"type": "spacer", "height": 0.2},
        {"type": "text", "content": "应对措施：", "style": "Heading2"},
        {"type": "text", "content": "• 增加后端开发人力投入，加班赶进度"},
        {"type": "text", "content": "• 提前启动部分模块的测试工作"},
        {"type": "text", "content": "• 与产品确认是否可以缩减非核心功能范围"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.add_data_source("progress", progress)
generator.save("examples/output/27_comprehensive_project.pdf")
print("✅ 已生成: examples/output/27_comprehensive_project.pdf")
