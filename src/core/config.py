from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

# string de conexion con la base de datos
    database_url: str = ''

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()