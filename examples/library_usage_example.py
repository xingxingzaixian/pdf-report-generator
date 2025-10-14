"""
PDF Report Generator - 库安装后的使用示例

演示如何在安装 pdf-report-generator 库后使用各种功能
"""

# ============================================================================
# 示例 1: 基础 PDF 生成
# ============================================================================

def example_1_basic_generation():
    """基础 PDF 生成示例"""
    print("\n=== 示例 1: 基础 PDF 生成 ===")
    
    from pdf_generator import PDFReportGenerator
    
    config = {
        "document": {
            "title": "基础示例报告",
            "pageSize": "A4",
            "author": "PDF Generator"
        },
        "content": [
            {
                "type": "text",
                "content": "欢迎使用 PDF Report Generator",
                "style": "Heading1"
            },
            {
                "type": "text",
                "content": "这是一个通过库安装后生成的 PDF 文档。",
                "style": "Normal"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    output_file = "library_example_01_basic.pdf"
    generator.generate(output_file)
    
    print(f"✅ PDF 已生成: {output_file}")


# ============================================================================
# 示例 2: 使用数据源
# ============================================================================

def example_2_with_data():
    """使用数据源生成 PDF"""
    print("\n=== 示例 2: 使用数据源 ===")
    
    from pdf_generator import PDFReportGenerator
    import pandas as pd
    
    # 准备数据
    sales_data = pd.DataFrame({
        "产品": ["产品A", "产品B", "产品C"],
        "销量": [100, 150, 200],
        "收入": [10000, 15000, 20000]
    })
    
    config = {
        "document": {
            "title": "销售报告",
            "pageSize": "A4"
        },
        "content": [
            {
                "type": "text",
                "content": "2024年销售报告",
                "style": "Heading1"
            },
            {
                "type": "table",
                "dataSource": "sales",
                "style": {
                    "headerStyle": {
                        "fillColor": "#4472C4",
                        "textColor": "#FFFFFF"
                    }
                }
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.add_data_source("sales", sales_data)
    
    output_file = "library_example_02_data.pdf"
    generator.generate(output_file)
    
    print(f"✅ PDF 已生成: {output_file}")


# ============================================================================
# 示例 3: 生成 PDF 字节流（不保存文件）
# ============================================================================

def example_3_to_bytes():
    """生成 PDF 字节流"""
    print("\n=== 示例 3: 生成 PDF 字节流 ===")
    
    from pdf_generator import PDFReportGenerator
    
    config = {
        "document": {
            "title": "字节流示例",
            "pageSize": "A4"
        },
        "content": [
            {
                "type": "text",
                "content": "这个 PDF 首先生成为字节流",
                "style": "Heading1"
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    pdf_bytes = generator.to_bytes()
    
    print(f"✅ PDF 字节流已生成，大小: {len(pdf_bytes)} 字节")
    
    # 可以将字节流保存到文件
    with open("library_example_03_bytes.pdf", "wb") as f:
        f.write(pdf_bytes)
    
    print("✅ 字节流已保存到文件")
    
    return pdf_bytes


# ============================================================================
# 示例 4: 启动 API 服务器（程序化）
# ============================================================================

def example_4_api_server():
    """启动 API 服务器示例"""
    print("\n=== 示例 4: 启动 API 服务器 ===")
    
    try:
        from pdf_generator import start_api_server
        
        print("正在启动 API 服务器...")
        print("访问 http://localhost:8080/docs 查看 API 文档")
        print("按 Ctrl+C 停止服务器")
        
        # 启动服务器（这会阻塞执行）
        start_api_server(
            host="localhost",
            port=8080,
            reload=True  # 开发模式
        )
        
    except ImportError:
        print("❌ API 依赖未安装")
        print("请运行: pip install pdf-report-generator[api]")
    except KeyboardInterrupt:
        print("\n✅ 服务器已停止")


# ============================================================================
# 示例 5: 获取 FastAPI 应用实例（自定义配置）
# ============================================================================

def example_5_custom_app():
    """获取并自定义 FastAPI 应用"""
    print("\n=== 示例 5: 自定义 FastAPI 应用 ===")
    
    try:
        from pdf_generator import create_app
        
        # 获取应用实例
        app = create_app()
        
        # 添加自定义路由
        @app.get("/custom/hello")
        async def custom_hello():
            return {"message": "Hello from custom endpoint!"}
        
        @app.get("/custom/info")
        async def custom_info():
            return {
                "app": "PDF Report Generator",
                "custom_endpoint": True
            }
        
        print("✅ FastAPI 应用已创建并添加自定义路由")
        print("自定义端点:")
        print("  - GET /custom/hello")
        print("  - GET /custom/info")
        
        # 可以使用 uvicorn 启动
        print("\n使用以下命令启动服务器:")
        print("  uvicorn your_module:app --host 0.0.0.0 --port 8000")
        
        return app
        
    except ImportError:
        print("❌ API 依赖未安装")
        print("请运行: pip install pdf-report-generator[api]")


# ============================================================================
# 示例 6: 从 JSON 文件生成 PDF
# ============================================================================

def example_6_from_json_file():
    """从 JSON 配置文件生成 PDF"""
    print("\n=== 示例 6: 从 JSON 文件生成 PDF ===")
    
    from pdf_generator import PDFReportGenerator
    import json
    
    # 假设有一个配置文件
    config_file = "templates/sales_report.json"
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        generator = PDFReportGenerator(config_dict=config)
        output_file = "library_example_06_from_json.pdf"
        generator.generate(output_file)
        
        print(f"✅ PDF 已从配置文件生成: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ 配置文件不存在: {config_file}")
    except Exception as e:
        print(f"❌ 生成失败: {e}")


# ============================================================================
# 示例 7: 完整的报告生成（图表 + 表格 + 样式）
# ============================================================================

def example_7_comprehensive_report():
    """生成包含图表、表格和样式的完整报告"""
    print("\n=== 示例 7: 完整报告生成 ===")
    
    from pdf_generator import PDFReportGenerator
    import pandas as pd
    
    # 准备数据
    monthly_data = pd.DataFrame({
        "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
        "销售额": [120000, 135000, 150000, 145000, 160000, 175000],
        "成本": [80000, 85000, 90000, 88000, 95000, 100000]
    })
    
    config = {
        "document": {
            "title": "月度经营报告",
            "pageSize": "A4",
            "author": "财务部"
        },
        "styles": {
            "customTitle": {
                "fontSize": 24,
                "textColor": "#2E4057",
                "alignment": "CENTER",
                "spaceAfter": 20
            }
        },
        "content": [
            {
                "type": "text",
                "content": "2024年上半年经营报告",
                "style": "customTitle"
            },
            {
                "type": "text",
                "content": "销售趋势分析",
                "style": "Heading2"
            },
            {
                "type": "chart",
                "chartType": "line",
                "dataSource": "monthly",
                "options": {
                    "x": "月份",
                    "y": ["销售额", "成本"],
                    "title": "销售额与成本趋势",
                    "width": 400,
                    "height": 250
                }
            },
            {
                "type": "text",
                "content": "详细数据",
                "style": "Heading2"
            },
            {
                "type": "table",
                "dataSource": "monthly",
                "style": {
                    "headerStyle": {
                        "fillColor": "#2E4057",
                        "textColor": "#FFFFFF",
                        "fontSize": 12
                    },
                    "cellStyle": {
                        "fontSize": 10
                    }
                }
            }
        ]
    }
    
    generator = PDFReportGenerator(config_dict=config)
    generator.add_data_source("monthly", monthly_data)
    
    output_file = "library_example_07_comprehensive.pdf"
    generator.generate(output_file)
    
    print(f"✅ 完整报告已生成: {output_file}")


# ============================================================================
# 主函数
# ============================================================================

def main():
    """运行所有示例"""
    print("=" * 70)
    print("PDF Report Generator - 库使用示例")
    print("=" * 70)
    
    # 运行示例
    example_1_basic_generation()
    example_2_with_data()
    example_3_to_bytes()
    # example_4_api_server()  # 这个会阻塞，所以默认注释掉
    example_5_custom_app()
    example_6_from_json_file()
    example_7_comprehensive_report()
    
    print("\n" + "=" * 70)
    print("所有示例执行完成！")
    print("=" * 70)
    print("\n提示:")
    print("  - 要启动 API 服务器，取消注释 example_4_api_server()")
    print("  - 或直接运行: pdf-report-api")
    print("  - API 文档: http://localhost:8000/docs")


if __name__ == "__main__":
    main()

