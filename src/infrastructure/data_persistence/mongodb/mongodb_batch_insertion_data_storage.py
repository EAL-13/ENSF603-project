from src.domain.article import Article

from src.infrastructure.data_persistence.mongodb.mongodb_data_storage import MongoDBDataStorage


class MongoDBBatchInsertionDataStorage(MongoDBDataStorage):
    __persistence_threshold = 100
    __cache_articles: dict = dict()
    __cache_hashes: set[str] = set()
    __cache_len: int = 0

    def persist_article(self, article: Article):
        if self.__cache_len < self.__persistence_threshold:
            self.__cache_articles[article.get_hash()] = article.to_dict()
            self.__cache_hashes.add(article.get_hash())
            self.__cache_len += 1
        else:
            try:
                if not self._uses_unique_index:
                    query = {"hash": {"$in": list(self.__cache_hashes)}}
                    for document in list(self._collection.find(query)):
                        del self.__cache_articles[document["hash"]]

                self._collection.insert_many(list(self.__cache_articles.values()), ordered=False)
            except:
                pass
            self.__cache_articles.clear()
            self.__cache_hashes.clear()
            self.__cache_len = 0
