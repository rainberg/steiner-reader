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

    # Credit pricing — per-sentence coefficient (overridden by credit_settings table)
    CREDIT_TRANSLATE_COEFFICIENT: float = 1.0
    CREDIT_EDIT_TRANSLATION_COEFFICIENT: float = 0.5
    CREDIT_EDIT_SOURCE_COEFFICIENT: float = 0.5
    CREDIT_DOWNLOAD_LECTURE_PRICE: int = 0
    CREDIT_DOWNLOAD_BOOK_PRICE: int = 0

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
