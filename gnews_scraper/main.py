from gnews_scraper import GoogleNewsScraper

from gnews_scraper.database import (
    connect_mongodb,
    connect_mysql,
    connect_postgres,
    connect_sqlite,
)

if __name__ == "__main__":
    query = "Machine Learning"

    google_news_scraper = GoogleNewsScraper(query, num_responses=5)
    articles = google_news_scraper.scrape_articles()

    # Pretty print articles
    google_news_scraper.print_articles(articles)

    # Save articles as a csv file

    # file_path = "dataset.csv"
    # google_news_scraper.to_csv(articles, file_path)

    # Save articles to a mongodb instance
    # username = "kishore-dev"
    # password = "26021999@Ks"
    # connection_uri = "mongodb+srv://%s:%s@google-news-scraper.tezquy7.mongodb.net/?retryWrites=true&w=majority"

    # db_name = "scraper_db"
    # collection_name = "news_articles"

    # collection = connect_mongodb(
    #     username, password, connection_uri, db_name, collection_name
    # )

    # google_news_scraper.to_mongodb(collection)

    # Save articles to postgres database
    # username = "postgres"
    # password = "postgres"
    # db_host = "localhost"
    # port = 5432
    # db_name = "google_news_scraper"
    # table_name = "articles"

    # engine = connect_postgres(username, password, db_host, port, db_name)

    # google_news_scraper.to_sql(table_name, engine)

    # Save articles to mysql / mariadb database
    # username = "root"
    # password = "password"
    # db_host = "localhost"
    # port = 3306
    # db_name = "google_news_scraper"
    # table_name = "articles"

    # engine = connect_mysql(username, password, db_host, port, db_name)

    # google_news_scraper.to_sql(table_name, engine)

    # Save articles to sqlite database
    # file_path = "./google_news_scraper.db"
    # table_name = "articles"

    # engine = connect_sqlite(file_path)

    # google_news_scraper.to_sql(table_name, engine)
