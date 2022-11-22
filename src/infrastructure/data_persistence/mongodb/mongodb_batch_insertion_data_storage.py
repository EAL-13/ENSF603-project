from src.domain.article import Article

from src.infrastructure.data_persistence.mongodb.mongodb_data_storage import MongoDBDataStorage


class MongoDBBatchInsertionDataStorage(MongoDBDataStorage):
    __persistence_threshold = 100
    __cache: list[dict] = list()
    __cache_len: int = 0

    def persist_article(self, article: Article):
        if self.__cache_len < self.__persistence_threshold:
            self.__cache.append(article.to_dict())
            self.__cache_len += 1
        else:
            try:
                self._collection.insert_many(self.__cache, False)
            except:
                pass
            self.__cache.clear()
            self.__cache_len = 0
