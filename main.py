# main.py - 根级入口，兼容 `uvicorn main:app` 启动方式
# src-layout: src/ 已加入 sys.path，app 包可直接导入
from app.main import app

__all__ = ["app"]