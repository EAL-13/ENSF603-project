from src.domain.data_persistence.data_storage import DataStorage
from src.domain.article import Article
import pymongo


class MongoDBSingleInsertionDataStorage(DataStorage):

    __client = pymongo.MongoClient("mongodb://localhost:27017/")
    __db = __client["ensf603"]
    __collection = __db["articles"]

    def persist_article(self, article: Article):
        self.__collection.insert_one(article.to_dict())
