"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://steiner:change_me@localhost:5432/steiner_reader"

    # Translation (Google Translate -- free, no API key needed)
    TRANSLATION_ENGINE: str = "google"

    # Auth Service
    AUTH_SERVICE_URL: str = "https://auth.3mudi.com"
    AUTH_APP_NAME: str = "steiner"

    # File storage
    UPLOAD_DIR: str = "/opt/steiner-reader/uploads"

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()
