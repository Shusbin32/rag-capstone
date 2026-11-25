from dataclasses import dataclass, field
from enum import Enum

from pydantic import BaseModel, Field

class DocumentType(Enum):
    TEXT = "text"
    MARKDOWN = "markdown"
    
@dataclass
class Document:
    source: str
    text: str 
    doc_type : DocumentType = DocumentType.TEXT
    metadata: dict = field(default_factory= dict)
    
    @property
    def word_count(self) -> int:
        return len(self.text.split())
 
class Question(BaseModel):
    text: str = Field(min_length=3)
    top_k: int = Field(default=3, ge=1, le=20)
