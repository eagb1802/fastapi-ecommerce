from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

# string de conexion con la base de datos
    database_url: str = 'postgresql+psycopg://postgres:31379381@localhost:5432/ecommerce_db'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()