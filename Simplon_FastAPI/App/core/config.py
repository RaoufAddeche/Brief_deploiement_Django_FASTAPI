# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str 
    DATABASE_URL: str 
    MODEL_PATH: str
    DB_SERVER : str
    DB_NAME: str 
    DB_USER: str 
    DB_PASSWORD: str 
    DB_DRIVER: str 
    

    class Config:
        env_file = ".env"

settings = Settings()

import os

print("Environment variables:")
for key, value in os.environ.items():
    print(f"{key}={value}")
