import time
from random import uniform
from threading import Thread

from src.domain.data_persistence.data_storage import DataStorage
from src.domain.scraper.article_scraper import ArticleScraper


class ThreadScraper(Thread):

    def __init__(self, data_storage: DataStorage, article_scraper: ArticleScraper):
        super().__init__()
        self.__active_thread = True
        self.__nbr_insertions_attempted = 0
        self.__data_storage = data_storage
        self.__article_scraper = article_scraper

    def run(self):
        while self.__active_thread:
            try:
                self.__data_storage.persist_article(self.__article_scraper.gatherArticle())
                self.__nbr_insertions_attempted += 1
                time.sleep(uniform(0.01, 0.1))
            except:
                break

    def stop_thread_and_gather_nbr_insertion_attempts(self):
        self.__active_thread = False
        return self.__nbr_insertions_attempted
