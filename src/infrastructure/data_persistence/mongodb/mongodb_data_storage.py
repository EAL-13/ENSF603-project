import threading

from abc import ABC
from src.domain.data_persistence.data_storage import DataStorage
import pymongo


class MongoDBDataStorage(DataStorage, ABC):
    __client = pymongo.MongoClient("mongodb://localhost:27017/")
    __db = __client["ensf603"]
    _collection = __db["articles"]

    def reset(self):
        self._collection.delete_many({})
