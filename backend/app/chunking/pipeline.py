from app.chunking.fixed_chunker import FixedChunker
from app.chunking.recursive_chunker import RecursiveChunker
from app.chunking.semantic_chunker import SemanticChunker


class ChunkingPipeline:
    def process(self, document, method="recursive", chunk_size=512):
        if method == "fixed":
            return (
                FixedChunker(chunk_size).chunk(document)
            )
        elif method == "semantic":
            return (
                SemanticChunker().chunk(document)
            )

        return (
            RecursiveChunker(chunk_size).chunk(document)
        )