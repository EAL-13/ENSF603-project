from abc import ABC, abstractmethod


class ArticleScraper(ABC):

    @abstractmethod
    def gatherArticle(self):
        pass
