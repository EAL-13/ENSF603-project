from abc import ABC, abstractmethod

from src.domain.article import Article


class DataStorage(ABC):

    @abstractmethod
    def persist_article(self, article: Article):
        pass

    @abstractmethod
    def reset(self, unique_index: bool):
        pass

    @abstractmethod
    def disable(self):
        pass
