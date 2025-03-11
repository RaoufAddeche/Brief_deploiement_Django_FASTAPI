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

# from pydantic_settings import BaseSettings
# from typing import Optional

# class Settings(BaseSettings):
#     # Variables de base de données
#     DB_SERVER: str
#     DB_NAME: str
#     DB_USER: str
#     DB_PASSWORD: str
#     DB_DRIVER: str

#     # Variables d'authentification
#     SECRET_KEY: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
#     ALGORITHM: str = "HS256"

#     # Chemin du modèle
#     MODEL_PATH: str = "model"

#     # Construction de l'URL de la base de données
#     @property
#     def DATABASE_URL(self) -> str:
#         return f"mssql+pyodbc://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}?driver={self.DB_DRIVER}"

#     class Config:
#         env_file = ".env"
#         case_sensitive = True

# # Instance des paramètres
# settings = Settings()