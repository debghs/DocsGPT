from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    LLM_NAME: str = "openai_chat"
    EMBEDDINGS_NAME: str = "openai_text-embedding-ada-002"
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    MONGO_URI: str

    API_URL: str = "http://localhost:5001"  # backend url for celery worker

    API_KEY: str = None  # LLM api key
    EMBEDDINGS_KEY: str = None  # api key for embeddings (if using openai, just copy API_KEY


path = Path(__file__).parent.parent.absolute()
settings = Settings(_env_file=path.joinpath(".env"), _env_file_encoding="utf-8")
