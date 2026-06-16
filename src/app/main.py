# main.py - FastAPI 应用入口
# Phase 1 核心路由：POST /api/v1/tasks 提交需求，GET /api/v1/tasks/{id} 查询状态
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO: 启动时初始化 DB engine + Chroma client
    yield
    # TODO: 关闭时释放 DB 连接 + Chroma 连接


app = FastAPI(title="StarRing-Dev", version="0.1.0", lifespan=lifespan)
app.include_router(api_router, prefix="/api/v1")