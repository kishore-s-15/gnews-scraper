# Importing the required libraries

import sys
import pprint
import logging
from datetime import datetime
from typing import Dict, List, Union

import requests
import pandas as pd
from bs4 import BeautifulSoup

from sqlalchemy.engine import Engine
from pymongo.collection import Collection

from gnews_scraper.utils.constants import (
    GOOGLE_NEWS_RSS_URL,
    GOOGLE_NEWS_DATETIME_FORMAT,
    MIN_RESPONSES,
    MAX_RESPONSES,
    DEFAULT_NUM_RESPONSES,
)

# Return type of google news article
GoogleNewsArticle = Dict[str, Union[str, datetime]]


class GoogleNewsScraper:
    """
    GoogleNewsScraper scrapes articles from google news rss feeds.
    """

    # Constants
    BASE_URL = GOOGLE_NEWS_RSS_URL
    DATE_TIME_FORMAT = GOOGLE_NEWS_DATETIME_FORMAT

    def __init__(self, query: str, num_responses: int = DEFAULT_NUM_RESPONSES):
        """
        Constuctor method initializes GoogleNewsScraper object
        to scrape google news rss feeds for the given query.

        Args:
            query (str): Query to scrape.
        """

        self.setup_logger()

        self.query = query
        self.url = f"{self.BASE_URL}?q={query}"

        self.num_responses = num_responses

        self.pretty_printer = pprint.PrettyPrinter()

    @property
    def query(self):
        """
        Getter method for _query attribute.
        """

        return self._query

    @property
    def num_responses(self):
        """
        Getter method for _num_responses attribute.
        """
        return self._num_responses

    @query.setter
    def query(self, query_string: str):
        """
        Setter method for _query attribute.

        Args:
            query_string (str): Query to scrape.
        """

        if query_string is None:
            error_message = "Query string is required."

            self.logger.error(error_message)
            raise ValueError(error_message)

        query_string_list = query_string.split(" ")
        query_string_list = list(map(lambda x: x.lower(), query_string_list))

        query_string = "+".join(query_string_list)

        self._query = query_string

    @num_responses.setter
    def num_responses(self, n: int):
        f"""
        Setter method for _num_responses attribute.

        Args:
            n (int): Number of responses.

        Raises:
            ValueError: If n is lesser than {MIN_RESPONSES} or greater than {MAX_RESPONSES}.
        """

        if n < MIN_RESPONSES:
            error_message = f"Num of responses should atleast be {MIN_RESPONSES}. But it is given as {n}."

            self.logger.error(error_message)
            raise ValueError(error_message)

        elif n > MAX_RESPONSES:
            error_message = f"Num of responses should atmost be {MAX_RESPONSES}. But it is given as {n}."

            self.logger.error(error_message)
            raise ValueError(error_message)

        self._num_responses = n

    def setup_logger(self):
        """
        Method sets up the logger.
        """

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        self.logger.info("Logger initialized.")

    def parse_string_to_datetime(self, date_time_str: str) -> datetime:
        """
        Method parses string to python datetime object.

        Args:
            date_time_str (str): Datetime string.

        Returns:
            date_time_obj (datetime): Parsed python datetime object.
        """

        date_time_obj = datetime.strptime(date_time_str, self.DATE_TIME_FORMAT)
        return date_time_obj

    def scrape_articles(self) -> List[GoogleNewsArticle]:
        """
        Method scrapes google news rss feed articles.

        Returns:
            articles (List[GoogleNewsArticle]): List of scraped articles of type GoogleNewsArticle.
        """

        self.logger.info(f"Started scraping {self.url}...")

        xml_content = requests.get(self.url).content
        soup = BeautifulSoup(xml_content, features="xml")
        items = soup.find_all("item")

        self.logger.info(f"Scraped {len(items)} articles.")

        articles: List[GoogleNewsArticle] = []

        for item in items:
            article = {}

            # Articles Info
            article["link"] = item.find("link").text
            article["title"] = item.find("title").text

            # Publisher info
            article["publisher"] = item.find("source").text
            article["published_date"] = self.parse_string_to_datetime(
                item.find("pubDate").text
            )

            articles.append(article)

        articles = articles[: self.num_responses]

        self.articles_df = pd.DataFrame(articles)

        return articles

    def print_articles(self, articles: List[GoogleNewsArticle]):
        """
        Method pretty prints scraped articles.

        Args:
            articles (List[GoogleNewsArticle]): Scraped Articles.
        """

        self.pretty_printer.pprint(articles)

    def to_csv(self, file_path: str):
        """
        Method saves the google news articles as a csv file to the specified file path.

        Args:
            file_path (str): File path
        """

        self.articles_df.to_csv(file_path, index=False)

    def to_mongodb(self, collection: Collection):
        """
        Method saves the google news articles to the MongoDB Collection.

        Args:
            collection (Collection): MongoDB Collection
        """

        collection.insert_many(self.articles_df.to_dict("records"))

    def to_sql(self, table_name: str, engine: Engine):
        """
        Method saves the google news articles to the table specified using the connection object.

        Args:
            table_name (str): Table Name.
            engine (Engine): sqlalchemy.engine.Engine
        """

        self.articles_df.to_sql(table_name, engine, if_exists="append")
