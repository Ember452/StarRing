# main.py - 根级入口，兼容 `uvicorn main:app` 启动方式
from app.main import app

__all__ = ["app"]