import string
from datetime import date
from random import randint, choice

from src.domain.article import Article
from src.domain.scraper.article_scraper import ArticleScraper


class SimulationArticleScraper(ArticleScraper):
    __letters = string.ascii_lowercase
    __inner_counter: int = 1

    def __init__(self):
        self.__expected_duplicate = Article(self.__generate_source(), self.__generate_author(), self.__generate_date(),
                                            self.__generate_body())

    def gatherArticle(self):
        # simulates duplication
        if self.__inner_counter % 5 == 0:
            self.__inner_counter = 1
            return self.__expected_duplicate

        # generate source
        source = self.__generate_source()

        # generate author

        author = self.__generate_author()

        # generate date
        article_date = self.__generate_date()

        # generate body of article
        body = self.__generate_body()

        self.__inner_counter += 1

        return Article(source, author, article_date, body)

    def __generate_source(self):
        nbr_words = randint(1, 20)
        title = ""
        for x in range(nbr_words):
            title += "".join(choice(self.__letters) for x in range(randint(1, 12)))
            title += "_"
        domain = "".join(choice(self.__letters) for x in range(randint(6, 20)))
        source = 'https://' + domain + '/' + title
        return source

    def __generate_author(self):
        author = ""
        author += "".join(choice(self.__letters) for x in range(randint(1, 12)))
        author += " "
        author += "".join(choice(self.__letters) for x in range(randint(1, 12)))
        return author

    def __generate_date(self):
        return date(randint(2000, 2022), randint(1, 12), randint(1, 27)).isoformat()

    def __generate_body(self):
        nbr_words = randint(400, 800)
        body = ""
        for x in range(nbr_words):
            body += "".join(choice(self.__letters) for x in range(randint(1, 12)))
            if x % 7 == 0:
                body += ". "
            else:
                body += " "
        body += ". "

        return body
