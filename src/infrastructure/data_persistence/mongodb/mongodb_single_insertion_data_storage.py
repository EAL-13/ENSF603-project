from src.domain.article import Article
from src.infrastructure.data_persistence.mongodb.mongodb_data_storage import MongoDBDataStorage


class MongoDBSingleInsertionDataStorage(MongoDBDataStorage):

    def persist_article(self, article: Article):
        self._validate_access()

        query = {"hash": article.get_hash()}
        if self._uses_unique_index or self._collection.find_one(query) == None:
            try:
                self._collection.insert_one(article.to_dict())
            except:
                pass
