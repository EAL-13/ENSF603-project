from src.domain.scraper.article_scraper_factory import ArticleScraperFactory
from src.domain.scraper.simulation_article_scraper import SimulationArticleScraper


class SimulationArticleScraperFactory(ArticleScraperFactory):

    def create(self):
        return SimulationArticleScraper()
