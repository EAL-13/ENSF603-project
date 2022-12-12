from abc import ABC

import pymongo

from src.domain.data_persistence.data_storage import DataStorage


class MongoDBDataStorage(DataStorage, ABC):
    __username = "lou"
    __password = "very!ation3"
    __url = "18.211.38.212"  # localhost For Local Instances
    __port = "27017"
    __db_name = "ensf603"

    __client = pymongo.MongoClient(
        "mongodb://" + __username + ":" + __password + "@" + __url + ":" + __port + "/" + __db_name)
    __db = __client["ensf603"]
    _collection = __db["articles"]

    __unique_index_field_name = "hash"
    _uses_unique_index = False

    def reset(self, unique_index: bool):
        self._uses_unique_index = unique_index

        query = {"date": {"$gte": "2000-01-01"}}
        self._collection.delete_many(query)

        self._collection.drop_indexes()
        if unique_index:
            self._collection.create_index(self.__unique_index_field_name, unique=True)
