from threading import Thread

from src.domain.data_persistence.data_storage import DataStorage
from src.domain.scraper.article_scraper import ArticleScraper


class ThreadScraper(Thread):

    def __init__(self, data_storage: DataStorage, article_scraper: ArticleScraper):
        super().__init__()
        self.__active_thread = True
        self.__data_storage = data_storage
        self.__article_scraper = article_scraper

    def run(self):
        while self.__active_thread:
            self.__data_storage.persist_article(self.__article_scraper.gatherArticle())

    def stop_thread(self):
        self.__active_thread = False
