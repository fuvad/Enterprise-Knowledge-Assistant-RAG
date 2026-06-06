from pydantic import BaseModel
from typing import List

from app.schemas.metadata import Metadata


class Document(BaseModel):
    source: str
    filename: str
    text: str
    
    metadata: Metadata | None = None