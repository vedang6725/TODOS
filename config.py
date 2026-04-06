from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL : str
    PAGE_SIZE : int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
 
 
settings = Settings()