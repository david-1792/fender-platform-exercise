import secrets

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env'
    )
    
    # API settings
    API_PREFIX: str = '/api'

    # Authentication settings
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database settings (DynamoDB)
    AWS_REGION: str = 'us-east-1'
    AWS_DDB_ENDPOINT: str = 'http://localhost:8000'
    AWS_DDB_TABLE_NAME: str = 'fender'

settings = Settings()