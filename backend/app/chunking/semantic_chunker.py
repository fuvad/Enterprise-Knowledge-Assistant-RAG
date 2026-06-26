from langchain_experimental.text_splitter import SemanticChunker as LCSemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from app.schemas.chunk import Chunk

class SemanticChunker:
    def __init__(self):
        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        self.splitter = LCSemanticChunker(
            embeddings,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=80
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