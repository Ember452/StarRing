# health.py - 健康检查接口
# GET /api/v1/health  - 服务存活 + DB/Chroma 连通性检查
from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check():
    # TODO: ping DB + Chroma，返回各组件状态
    return {"status": "ok"}