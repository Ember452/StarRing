# tasks.py - 任务管理接口
# POST /api/v1/tasks       - 提交自然语言需求，启动编排流水线
# GET  /api/v1/tasks/{id}  - 查询任务状态 + 输出文件列表
from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def create_task():
    # TODO: 接收需求文本 → 创建 Task → 触发 pipeline.run()
    return {"message": "not implemented"}


@router.get("/{task_id}")
async def get_task(task_id: str):
    # TODO: 查询任务状态 + 生成文件列表
    return {"task_id": task_id, "message": "not implemented"}