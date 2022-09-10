import urllib

from pymongo import MongoClient
from pymongo.collection import Collection


def connect_mongodb(
    username: str,
    password: str,
    connection_uri: str,
    db_name: str,
    collection_name: str,
) -> Collection:

    username = urllib.parse.quote(username)
    password = urllib.parse.quote(password)

    MONGODB_URI = connection_uri % (username, password)

    client = MongoClient(MONGODB_URI)

    db = client[db_name]
    collection = db[collection_name]

    return collection
