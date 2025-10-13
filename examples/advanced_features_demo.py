"""高级功能演示：页眉页脚、目录、封面"""

import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pdf_generator import PDFReportGenerator


def example1_header_footer():
    """示例1：页眉页脚功能"""
    
    config = {
        "metadata": {
            "title": "页眉页脚演示",
            "author": "PDF Generator",
            "company": "示例公司"
        },
        "pageTemplate": {
            "header": {
                "enabled": True,
                "height": 0.8,
                "showLine": True,
                "left": {
                    "type": "text",
                    "content": "{{metadata.title}}",
                    "fontSize": 9
                },
                "center": {
                    "type": "text",
                    "content": "内部文档",
                    "fontSize": 9
                },
                "right": {
                    "type": "text",
                    "content": "{{date}}",
                    "fontSize": 9
                }
            },
            "footer": {
                "enabled": True,
                "height": 0.6,
                "showLine": True,
                "left": {
                    "type": "text",
                    "content": "{{metadata.company}}",
                    "fontSize": 8
                },
                "center": {
                    "type": "pageNumber",
                    "format": "第{page}页 共{total}页",
                    "fontSize": 8
                },
                "right": {
                    "type": "text",
                    "content": "保密",
                    "fontSize": 8,
                    "color": "#FF0000"
                }
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "<b>页眉页脚功能演示</b>",
                "style": "Title"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "这个PDF演示了页眉页脚功能。注意页面顶部和底部的页眉页脚。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "页眉显示：<br/>- 左侧：文档标题<br/>- 中间：\"内部文档\"<br/>- 右侧：当前日期"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "页脚显示：<br/>- 左侧：公司名称<br/>- 中间：页码（第X页 共Y页）<br/>- 右侧：\"保密\"（红色）"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "text",
                "content": "<b>第二页</b>",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "在这一页，页眉页脚会自动更新页码。"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_header_footer.pdf")
    print("✅ 页眉页脚示例生成完成: output_header_footer.pdf")


def example2_toc_auto():
    """示例2：自动生成目录"""
    
    config = {
        "metadata": {
            "title": "自动目录演示"
        },
        "toc": {
            "enabled": True,
            "autoGenerate": True,
            "title": "目录",
            "maxLevel": 3
        },
        "elements": [
            {
                "type": "heading",
                "text": "第一章 引言",
                "level": 1
            },
            {
                "type": "text",
                "content": "这是第一章的内容。目录会自动生成，包含本文档的所有标题。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "1.1 背景",
                "level": 2
            },
            {
                "type": "text",
                "content": "这是1.1节的内容。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "1.2 目的",
                "level": 2
            },
            {
                "type": "text",
                "content": "这是1.2节的内容。"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "heading",
                "text": "第二章 主体内容",
                "level": 1
            },
            {
                "type": "text",
                "content": "这是第二章的内容。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "2.1 功能说明",
                "level": 2
            },
            {
                "type": "text",
                "content": "这是2.1节的内容。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "2.1.1 详细说明",
                "level": 3
            },
            {
                "type": "text",
                "content": "这是2.1.1节的内容（三级标题）。"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "heading",
                "text": "第三章 总结",
                "level": 1
            },
            {
                "type": "text",
                "content": "这是第三章的内容。本文档演示了自动目录生成功能。"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_toc_auto.pdf")
    print("✅ 自动目录示例生成完成: output_toc_auto.pdf")


def example3_cover_page():
    """示例3：封面页"""
    
    config = {
        "metadata": {
            "title": "年度报告",
            "author": "张三",
            "company": "示例科技有限公司"
        },
        "coverPage": {
            "enabled": True,
            "background": {
                "type": "gradient",
                "colorStart": "#1a1a2e",
                "colorEnd": "#16213e"
            },
            "elements": [
                {
                    "type": "text",
                    "content": "{{metadata.title}}",
                    "style": "Title",
                    "position": {"x": "center", "y": 500}
                },
                {
                    "type": "text",
                    "content": "{{metadata.company}}",
                    "style": "Heading1",
                    "position": {"x": "center", "y": 400}
                },
                {
                    "type": "text",
                    "content": "编制：{{metadata.author}}",
                    "style": "Normal",
                    "position": {"x": "center", "y": 200}
                },
                {
                    "type": "text",
                    "content": "{{date}}",
                    "style": "Normal",
                    "position": {"x": "center", "y": 150}
                }
            ]
        },
        "elements": [
            {
                "type": "heading",
                "text": "第一章 概述",
                "level": 1
            },
            {
                "type": "text",
                "content": "这个PDF演示了封面页功能。封面使用了渐变背景和多个文本元素。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "封面元素包括：<br/>- 报告标题<br/>- 公司名称<br/>- 编制人<br/>- 日期"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_cover_page.pdf")
    print("✅ 封面页示例生成完成: output_cover_page.pdf")


def example4_complete_report():
    """示例4：完整报告（封面+目录+页眉页脚）"""
    
    config = {
        "metadata": {
            "title": "2024年度业务分析报告",
            "author": "数据分析部",
            "company": "示例科技有限公司"
        },
        "coverPage": {
            "enabled": True,
            "background": {
                "type": "color",
                "color": "#FFFFFF"
            },
            "elements": [
                {
                    "type": "text",
                    "content": "{{metadata.title}}",
                    "style": "Title",
                    "position": {"x": "center", "y": 550}
                },
                {
                    "type": "text",
                    "content": "{{metadata.company}}",
                    "style": "Heading1",
                    "position": {"x": "center", "y": 450}
                },
                {
                    "type": "text",
                    "content": "编制部门：{{metadata.author}}",
                    "style": "Normal",
                    "position": {"x": "center", "y": 220}
                },
                {
                    "type": "text",
                    "content": "{{date}}",
                    "style": "Normal",
                    "position": {"x": "center", "y": 180}
                }
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
                "height": 0.8,
                "showLine": True,
                "left": {
                    "type": "text",
                    "content": "{{metadata.title}}"
                },
                "right": {
                    "type": "text",
                    "content": "{{date}}"
                }
            },
            "footer": {
                "enabled": True,
                "height": 0.6,
                "showLine": True,
                "center": {
                    "type": "pageNumber",
                    "format": "- {page} -"
                }
            }
        },
        "elements": [
            {
                "type": "heading",
                "text": "第一章 报告概述",
                "level": 1
            },
            {
                "type": "text",
                "content": "本报告综合展示了PDF生成器的高级功能，包括封面页、自动目录和页眉页脚。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "1.1 报告目的",
                "level": 2
            },
            {
                "type": "text",
                "content": "演示如何创建专业的PDF报告，包含完整的文档结构和样式。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "1.2 主要内容",
                "level": 2
            },
            {
                "type": "text",
                "content": "本报告包含以下主要内容：<br/>• 封面页设计<br/>• 自动目录生成<br/>• 页眉页脚配置<br/>• 多级标题结构"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "heading",
                "text": "第二章 功能说明",
                "level": 1
            },
            {
                "type": "text",
                "content": "本章详细说明各项功能的使用方法。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "2.1 封面页功能",
                "level": 2
            },
            {
                "type": "text",
                "content": "封面页支持：<br/>• 背景颜色/图片/渐变<br/>• 文本元素自由定位<br/>• 模板变量替换<br/>• 预设模板"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "2.2 目录功能",
                "level": 2
            },
            {
                "type": "text",
                "content": "目录功能支持：<br/>• 自动收集标题<br/>• 多级层级显示<br/>• 页码自动更新<br/>• 手动配置选项"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "heading",
                "text": "2.3 页眉页脚功能",
                "level": 2
            },
            {
                "type": "text",
                "content": "页眉页脚功能支持：<br/>• 左中右三栏布局<br/>• 文本/图片/页码<br/>• 变量替换<br/>• 多种页码格式"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "heading",
                "text": "第三章 总结",
                "level": 1
            },
            {
                "type": "text",
                "content": "本报告演示了PDF生成器的高级功能，这些功能可以帮助您创建专业、美观的PDF文档。"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "通过组合使用封面、目录和页眉页脚功能，您可以轻松生成符合企业标准的正式报告。"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_complete_report.pdf")
    print("✅ 完整报告示例生成完成: output_complete_report.pdf")


def example5_page_number_formats():
    """示例5：多种页码格式"""
    
    config = {
        "metadata": {
            "title": "页码格式演示"
        },
        "pageTemplate": {
            "footer": {
                "enabled": True,
                "height": 0.8,
                "left": {
                    "type": "pageNumber",
                    "format": "阿拉伯数字：{page}"
                },
                "center": {
                    "type": "pageNumber",
                    "format": "罗马数字：{page:roman}"
                },
                "right": {
                    "type": "pageNumber",
                    "format": "中文数字：第{page:chinese}页"
                }
            }
        },
        "elements": [
            {
                "type": "text",
                "content": "<b>页码格式演示</b>",
                "style": "Title"
            },
            {
                "type": "spacer",
                "height": 0.3
            },
            {
                "type": "text",
                "content": "查看页脚，可以看到三种不同的页码格式：<br/>• 左侧：阿拉伯数字<br/>• 中间：罗马数字<br/>• 右侧：中文数字"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "text",
                "content": "<b>第二页</b>",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "页码会自动更新为相应格式的数字。"
            },
            {
                "type": "pagebreak"
            },
            {
                "type": "text",
                "content": "<b>第三页</b>",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "支持的页码格式包括：<br/>• {page} 或 {page:arabic} - 阿拉伯数字<br/>• {page:roman} - 罗马数字（大写）<br/>• {page:roman_lower} - 罗马数字（小写）<br/>• {page:chinese} - 中文数字"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.save("output_page_formats.pdf")
    print("✅ 页码格式示例生成完成: output_page_formats.pdf")


if __name__ == "__main__":
    print("=" * 60)
    print("PDF高级功能演示")
    print("=" * 60)
    
    example1_header_footer()
    print()
    
    example2_toc_auto()
    print()
    
    example3_cover_page()
    print()
    
    example4_complete_report()
    print()
    
    example5_page_number_formats()
    print()
    
    print("=" * 60)
    print("所有示例已生成完成！")
    print("=" * 60)

