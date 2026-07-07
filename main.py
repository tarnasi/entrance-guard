from functools import lru_cache
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.api.auth import login, logout, profile, register


class ApplicationSetting(BaseSettings):
    
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3606
    MYSQL_USERNAME: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_URL: str

    JWT_SECRET: str
    JWT_EXPIRES: str
    
    model_config = SettingsConfigDict(env_file='.env')


@lru_cache
def get_settings():
    return ApplicationSetting()


app = FastAPI(
    title="Base Service Authentication and Authorization"
)

app.include_router(register.router, prefix="/api/auth")
app.include_router(login.router, prefix="/api/auth")
app.include_router(profile.router, prefix="/api/auth")
app.include_router(logout.router, prefix="/api/auth")


