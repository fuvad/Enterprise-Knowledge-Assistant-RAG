from pydantic import BaseModel


class Metadata(BaseModel):
    department: str | None = None
    tags: list[str] = []
    
    owner: str | None = None
    document_type: str | None = None
    security_level: str | None = None