from typing import Optional

import mongoengine
from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDB:
    def __init__(self, mongo_uri: str):
        self._connection = Optional[MongoClient] = None
        self.mongo_uri = mongo_uri

    def get_or_create_connection(self) -> MongoClient:
        if self._connection:
            return self._connection
        self._connection = mongoengine.connect(host=self.mongo_uri)
        return self._connection

    def get_collection(self, collection_name) -> Collection:
        connection = self.get_or_create_connection()
        db = connection.get_database()
        collection = db.get_collection(collection_name)
        return collection
