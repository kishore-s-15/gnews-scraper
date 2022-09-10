import pprint

import click
import pandas as pd

from gnews_scraper import GoogleNewsScraper
from gnews_scraper.utils.constants import (
    MIN_RESPONSES,
    MAX_RESPONSES,
    DEFAULT_NUM_RESPONSES,
)


@click.command()
@click.option("--query", help="Query to scrape")
@click.option(
    "--num_responses",
    default=DEFAULT_NUM_RESPONSES,
    help="Number of responses to return.",
)
@click.option(
    "--tabulate",
    default=False,
    help="Tabulates the scraped articles",
)
def scrape_google_news_articles(
    query: str,
    num_responses: click.IntRange(min=MIN_RESPONSES, max=MAX_RESPONSES),
    tabulate: click.BOOL,
):
    """
    Scrape Google news articles based on the given query.
    """

    google_news_scraper = GoogleNewsScraper(query, num_responses)

    articles = google_news_scraper.scrape_articles()

    if tabulate:
        pd.set_option("display.max_rows", None)
        pd.set_option("display.chop_threshold", 1)

        print(pd.DataFrame(articles))

    else:
        pretty_printer = pprint.PrettyPrinter()
        pretty_printer.pprint(articles)


if __name__ == "__main__":
    scrape_google_news_articles()
