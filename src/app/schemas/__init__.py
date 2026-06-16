# schemas - Pydantic 请求/响应序列化模型
# 与 models/ 分离，遵循关注点分离原则：
#   models/ = SQLAlchemy ORM（数据库映射）
#   schemas/ = Pydantic BaseModel（API 协议）