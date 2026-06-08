from abc import ABC
from abc import abstractmethod


class BaseEmbedder(ABC):
    @abstractmethod
    def embed(self, texts: list[str]):
        pass
    
#forces every embedding model to have or implement embed()