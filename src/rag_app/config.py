from enum import Enum
from pathlib import Path

from pydantic import Field, SecretStr , model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class LogLevel(str , Enum):
    DEBUG="DEBUG"
    INFO="INFO"
    WARNING="WARNING"
    ERROR="ERROR"
    
class Settings(BaseSettings):
   model_config= SettingsConfigDict(
       env_prefix="RAG_",
       env_file=".env",
       extra="ignore"      
   )
   app_name: str = "rag-capstone"
   data_dir: Path = Path("data")
   chunk_size: int = Field(default=500, gt=0)
   chunk_overlap: int = Field(default=50, ge=0)
   log_level: LogLevel = LogLevel.INFO
   llm_model: str = "your-model-name"
   llm_api_key: SecretStr | None = None
   
   @model_validator(mode="after")
   def check_overlap(self) -> "Settings":
       if self.chunk_overlap >= self.chunk_size:
           raise ValueError("chunk_overlap must be smaller than chunk_size")
       return self
       
def load_settings() -> Settings:
    return Settings()
        