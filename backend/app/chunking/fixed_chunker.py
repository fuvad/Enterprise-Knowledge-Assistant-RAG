from app.schemas.chunk import Chunk

class FixedChunker:
    def __init__(self, chunk_size=512):
        self.chunk_size = chunk_size

    def chunk(self, document):
        chunks = []
        text = document.text

        for i in range(0, len(text), self.chunk_size):
            chunk_text = text[i:i+self.chunk_size]
            
            chunks.append(
                Chunk(
                    chunk_id=len(chunks),
                    source=document.source,
                    filename=document.filename,
                    text=chunk_text,
                    metadata=document.metadata
                )
            )

        return chunks