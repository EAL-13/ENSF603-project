from src.application_service.thread_scraper import ThreadScraper
from src.domain.data_persistence.data_storage import DataStorage
from src.domain.scraper.article_scraper_factory import ArticleScraperFactory


class ScraperService:

    def __init__(self, data_storage: DataStorage, article_scraper_factory: ArticleScraperFactory):
        self.__data_storage: DataStorage = data_storage
        self.__article_scraper_factory: ArticleScraperFactory = article_scraper_factory
        self.__scraper_threads = set()

    def start(self, nbr_threads: int, unique_index: bool):
        if nbr_threads > 100:
            nbr_threads = 100

        self.stop_and_gather_nbr_insertion_attempts()
        self.__data_storage.reset(unique_index)

        for _ in range(nbr_threads):
            article_scraper = self.__article_scraper_factory.create()
            thread_scraper = ThreadScraper(self.__data_storage, article_scraper)
            thread_scraper.start()
            self.__scraper_threads.add(thread_scraper)

    def stop_and_gather_nbr_insertion_attempts(self):
        self.__data_storage.disable()
        insertion_attempts = 0

        for thread in self.__scraper_threads:
            insertion_attempts += thread.stop_thread_and_gather_nbr_insertion_attempts()
            thread.join()
        self.__scraper_threads.clear()

        return insertion_attempts
