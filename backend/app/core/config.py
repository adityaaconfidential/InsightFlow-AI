from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_port: int = 8000
    database_url: str = "postgresql://postgres:postgres@postgres:5432/insightflow"
    redis_url: str = "redis://redis:6379"
    secret_key: str = "replace_with_secure_secret"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
