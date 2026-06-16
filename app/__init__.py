# app - StarRing Phase 1 应用主包
#
# 分层架构（自顶向下）：
#   api/            - 接入层：FastAPI 路由、版本化接口
#   orchestration/  - 编排层：LangGraph StateGraph 流水线
#   agents/         - Agent 层：4 个业务 Agent
#   rag/            - 基础层：Chroma 代码向量检索
#   utils/          - 基础层：Agent 工具函数
#   models/         - 基础层：SQLAlchemy ORM 模型
#   schemas/        - 基础层：Pydantic 序列化模型
#   db/             - 基础层：数据库连接与会话
#   config/         - 配置中心：.env 加载、多环境配置
#   core/           - 横切层：全局异常处理、中间件、安全