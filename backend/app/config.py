"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://steiner:change_me@localhost:5432/steiner_reader"

    # Translation (Google Translate -- free, no API key needed)
    TRANSLATION_ENGINE: str = "google"  # google or deepseek

    # Auth
    JWT_SECRET_KEY: str = "change-me-in-env"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    # File storage
    UPLOAD_DIR: str = "/opt/steiner-reader/uploads"

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
