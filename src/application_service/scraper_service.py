from src.application_service.thread_scraper import ThreadScraper
from src.domain.data_persistence.data_storage import DataStorage
from src.domain.scraper.article_scraper_factory import ArticleScraperFactory


class ScraperService:

    def __init__(self, data_storage: DataStorage, article_scraper_factory: ArticleScraperFactory):
        self.__data_storage: DataStorage = data_storage
        self.__article_scraper_factory: ArticleScraperFactory = article_scraper_factory
        self.__scraper_threads = set()

    def start(self, nbr_threads):
        ThreadScraper.thread_stopped = False
        for _ in range(nbr_threads):
            article_scraper = self.__article_scraper_factory.create()
            thread_scraper = ThreadScraper(self.__data_storage, article_scraper)
            thread_scraper.start()
            self.__scraper_threads.add(thread_scraper)

    def stop(self):
        for thread in self.__scraper_threads:
            thread.stop_thread()
            thread.join()
        self.__scraper_threads.clear()