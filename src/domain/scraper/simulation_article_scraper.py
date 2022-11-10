from random import randint, choice
import string
from datetime import date

from src.domain.article import Article
from src.domain.scraper.article_scraper import ArticleScraper


class SimulationArticleScraper(ArticleScraper):
    __letters = string.ascii_lowercase

    def gatherArticle(self):
        # generate source
        nbr_words = randint(1, 20)
        domain = "".join(choice(self.__letters) for x in range(randint(6, 20)))
        title = ""
        for x in range(nbr_words):
            title += "".join(choice(self.__letters) for x in range(randint(1, 12)))
            title += "_"

        source = 'https://' + domain + '/' + title

        # generate author
        author = ""
        author += "".join(choice(self.__letters) for x in range(randint(1, 12)))
        author += " "
        author += "".join(choice(self.__letters) for x in range(randint(1, 12)))

        # generate date
        article_date = date(randint(2000, 2022), randint(1, 12), randint(1, 27)).isoformat()

        # generate text article
        nbr_words = randint(400, 800)
        body = ""
        for x in range(nbr_words):
            body += "".join(choice(self.__letters) for x in range(randint(1, 12)))
            if x % 7 == 0:
                body += ". "
            else:
                body += " "
        body += ". "

        return Article(source, author, article_date, body)
