# settings.py - 应用配置中心（基于 .env 文件 + pydantic-settings）
# TODO: 安装 pydantic-settings 后取消注释以下实现
# from pydantic_settings import BaseSettings, SettingsConfigDict
#
# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
#
#     # ── SiliconFlow API ──
#     siliconflow_api_key: str
#     siliconflow_base_url: str = "https://api.siliconflow.cn/v1"
#     llm_model: str = "deepseek-ai/DeepSeek-V4-Pro"
#
#     # ── Chroma 向量库 ──
#     chroma_persist_dir: str = "./data/chroma"
#
#     # ── SQLite 数据库 ──
#     database_url: str = "sqlite:///./data/starring.db"
#
#     # ── 生成文件输出 ──
#     storage_dir: str = "./storage"
#
#     # ── 服务配置 ──
#     server_host: str = "0.0.0.0"
#     server_port: int = 8000
#
# settings = Settings()