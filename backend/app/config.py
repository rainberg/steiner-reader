"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://steiner:password@db:5432/steiner_reader"

    # Translation (DeepSeek)
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    TRANSLATION_MODEL: str = "deepseek-chat"

    # File storage
    UPLOAD_DIR: str = "/app/uploads"

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
