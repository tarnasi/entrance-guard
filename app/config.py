from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class ApplicationSetting(BaseSettings):

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3606
    MYSQL_USERNAME: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_URL: str

    JWT_SECRET: str
    JWT_EXPIRES: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return ApplicationSetting()
