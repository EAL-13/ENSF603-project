from src.domain.article import Article
from src.infrastructure.data_persistence.mongodb.mongodb_data_storage import MongoDBDataStorage


class MongoDBSingleInsertionDataStorage(MongoDBDataStorage):

    def persist_article(self, article: Article):
        self._collection.insert_one(article.to_dict())
