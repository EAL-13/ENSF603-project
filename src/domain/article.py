class Article:

    def __init__(self, source: str, author: str, date: str, body: str):
        self.__source: str = source
        self.__author: str = author
        self.__date: str = date
        self.__body: str = body

    def to_dict(self):
        return {"source": self.__source, "author": self.__author, "date": self.__date, "body": self.__body}
