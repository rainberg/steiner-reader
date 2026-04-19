"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://steiner:password@db:5432/steiner_reader"

    # Translation (Google Translate — free, no API key needed)
    TRANSLATION_ENGINE: str = "google"  # google or deepseek

    # File storage
    UPLOAD_DIR: str = "/app/uploads"

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
