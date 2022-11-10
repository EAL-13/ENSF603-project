from abc import ABC, abstractmethod


class ArticleScraperFactory(ABC):

    @abstractmethod
    def create(self):
        pass
