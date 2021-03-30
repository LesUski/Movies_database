from pymongo import MongoClient
from .db_settings import *

client = MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}')
db = client.movie_dialogs_db


class Document:
    collection = None

    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def save(self):
        return self.collection.insert_one(self.__dict__).inserted_id

    @classmethod
    def get_all(cls):

        return [cls(**item) for item in cls.collection.find({})]

    @classmethod
    def find(cls, **kwargs):
        return [cls(**item) for item in cls.collection.find(kwargs)]