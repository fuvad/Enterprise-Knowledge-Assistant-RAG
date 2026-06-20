from pydantic import BaseModel
from app.schemas.metadata import Metadata


class Chunk(BaseModel):
    chunk_id: int
    source: str
    filename: str
    text: str
    metadata: Metadata | None = None