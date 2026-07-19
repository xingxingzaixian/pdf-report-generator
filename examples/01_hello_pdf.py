"""
01 - Hello PDF：5行代码生成第一个 PDF

这是最简单的入门示例，展示 PDF Report Generator 的核心用法。
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pdf_generator import PDFReportGenerator

config = {
    "metadata": {"title": "Hello PDF"},
    "elements": [
        {"type": "text", "content": "Hello, PDF Report Generator!"}
    ]
}

generator = PDFReportGenerator(config_dict=config)
generator.save("examples/output/01_hello.pdf")
print("✅ 已生成: examples/output/01_hello.pdf")
