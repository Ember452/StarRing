# router.py - API v1 路由聚合
from fastapi import APIRouter

from app.api.v1 import tasks, health

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(health.router, prefix="/health", tags=["health"])