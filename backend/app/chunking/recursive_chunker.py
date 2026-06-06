from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.schemas.chunk import Chunk


class RecursiveChunker:
    def __init__(self, chunk_size=512, chunk_overlap=50):
        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
        )

    def chunk(self, document):
        split_texts = self.splitter.split_text(document.text)

        chunks = []

        for idx, text in enumerate(split_texts):
            chunks.append(
                Chunk(
                    chunk_id=idx,
                    source=document.source,
                    filename=document.filename,
                    text=text,
                    metadata=document.metadata
                )
            )

        return chunks