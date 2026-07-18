"""
PDF Report Generator API Server

This module provides a simple way to start the API server programmatically.
"""

import os
import sys
from typing import Optional


def start_api_server(
    host: str = "0.0.0.0",
    port: int = 8000,
    reload: bool = False,
    log_level: str = "info",
    workers: int = 1,
):
    """
    启动 PDF Report Generator API 服务器
    
    Args:
        host: 服务器主机地址，默认 "0.0.0.0"
        port: 服务器端口，默认 8000
        reload: 是否启用热重载（开发模式），默认 False
        log_level: 日志级别 ("critical", "error", "warning", "info", "debug", "trace")，默认 "info"
        workers: 工作进程数量（生产环境），默认 1
        
    Example:
        >>> from pdf_generator import start_api_server
        >>> start_api_server(host="localhost", port=8080)
        
        或者在代码中：
        >>> if __name__ == "__main__":
        >>>     start_api_server(port=8080, reload=True)
    """
    try:
        import uvicorn
    except ImportError:
        raise ImportError(
            "FastAPI 和 Uvicorn 未安装。请运行: pip install pdf-report-generator[api]"
        )
    
    # 确保 api 模块可以被导入
    try:
        from pdf_generator.api.main import app
    except ImportError:
        # 尝试添加当前目录到 Python 路径
        current_dir = os.getcwd()
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        try:
            from pdf_generator.api.main import app
        except ImportError:
            raise ImportError(
                "无法导入 API 模块。请确保 'pdf_generator' 模块在 Python 路径中。"
            )
    
    print(f"🚀 启动 PDF Report Generator API 服务器...")
    print(f"📍 地址: http://{host}:{port}")
    print(f"📖 API 文档: http://{host}:{port}/docs")
    print(f"📚 ReDoc 文档: http://{host}:{port}/redoc")
    print(f"⚙️  模式: {'开发模式 (热重载)' if reload else '生产模式'}")
    print(f"👷 工作进程: {workers if not reload else 1}")
    print()
    
    uvicorn.run(
        "pdf_generator.api.main:app",
        host=host,
        port=port,
        reload=reload,
        log_level=log_level,
        workers=1 if reload else workers,  # reload 模式下只能单进程
    )


def create_app():
    """
    创建并返回 FastAPI 应用实例
    
    这个函数用于需要自定义配置 FastAPI 应用的场景
    
    Returns:
        FastAPI: FastAPI 应用实例
        
    Example:
        >>> from pdf_generator import create_app
        >>> app = create_app()
        >>> # 添加自定义中间件或路由
        >>> @app.get("/custom")
        >>> def custom_endpoint():
        >>>     return {"message": "Custom endpoint"}
    """
    try:
        from pdf_generator.api.main import app
        return app
    except ImportError:
        raise ImportError(
            "FastAPI 未安装。请运行: pip install pdf-report-generator[api]"
        )


__all__ = ["start_api_server", "create_app"]

