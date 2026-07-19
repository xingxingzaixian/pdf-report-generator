"""
14 - 自动目录：多级标题、自动页码

演示 toc 配置中 autoGenerate 自动生成目录。
使用 heading 元素定义标题层级，系统自动收集并生成目录页。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "自动目录演示"},
    "toc": {
        "enabled": True,
        "autoGenerate": True,
        "title": "目  录",
        "maxLevel": 3
    },
    "elements": [
        {"type": "heading", "text": "第一章 项目概述", "level": 1},
        {"type": "text", "content": "本章介绍项目的背景、目标和范围。"},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "1.1 项目背景", "level": 2},
        {"type": "text", "content": "项目背景的详细描述..."},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "1.2 项目目标", "level": 2},
        {"type": "text", "content": "项目目标的详细描述..."},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "1.2.1 短期目标", "level": 3},
        {"type": "text", "content": "短期目标：3个月内完成MVP版本。"},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "1.2.2 长期目标", "level": 3},
        {"type": "text", "content": "长期目标：12个月内达到100万用户。"},
        {"type": "pagebreak"},

        {"type": "heading", "text": "第二章 技术方案", "level": 1},
        {"type": "text", "content": "本章介绍技术架构和实现方案。"},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "2.1 系统架构", "level": 2},
        {"type": "text", "content": "采用微服务架构，前后端分离。"},
        {"type": "spacer", "height": 0.2},

        {"type": "heading", "text": "2.2 技术选型", "level": 2},
        {"type": "text", "content": "Python + FastAPI + React + PostgreSQL。"},
        {"type": "pagebreak"},

        {"type": "heading", "text": "第三章 总结与展望", "level": 1},
        {"type": "text", "content": "本文档演示了自动目录生成功能。"},
        {"type": "text", "content": "目录会自动收集所有 heading 元素，生成带页码的目录页。"},
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/14_toc.pdf")
print("✅ 已生成: examples/output/14_toc.pdf")
print("   打开 PDF 查看自动生成的目录页（位于封面之后）。")
