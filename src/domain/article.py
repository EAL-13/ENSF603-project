import random


class Article:

    def __init__(self, source: str, author: str, date: str, body: str):
        self.__source: str = source
        self.__author: str = author
        self.__date: str = date
        self.__body: str = body

        if random.randint(1, 10) <= 5:
            self.__hash: str = "duplication"
        else:
            self.__hash: str = str(hash((source, author, date, body)))

    def to_dict(self):
        return {"source": self.__source, "author": self.__author, "date": self.__date, "body": self.__body,
                "hash": self.__hash}
