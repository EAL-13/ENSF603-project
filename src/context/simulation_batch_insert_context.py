from src.application_service.scraper_service import ScraperService
from src.domain.data_persistence.data_storage import DataStorage
from src.domain.scraper.article_scraper_factory import ArticleScraperFactory
from src.domain.scraper.simulation_article_scraper_factory import SimulationArticleScraperFactory
from src.infrastructure.data_persistence.mongodb.mongodb_batch_insertion_data_storage import \
    MongoDBBatchInsertionDataStorage

__data_storage: DataStorage = MongoDBBatchInsertionDataStorage()
__article_scraper_factory: ArticleScraperFactory = SimulationArticleScraperFactory()

scraper_service: ScraperService = ScraperService(__data_storage, __article_scraper_factory)
