"""Application settings loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://steiner:password@db:5432/steiner_reader"

    # Translation (api2d.net)
    API2D_API_KEY: str = ""
    API2D_BASE_URL: str = "https://openai.api2d.net/v1"
    TRANSLATION_MODEL: str = "gpt-4o"

    # File storage
    UPLOAD_DIR: str = "/app/uploads"

    # App
    APP_NAME: str = "Steiner Reader"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
