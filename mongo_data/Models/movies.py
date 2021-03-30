from mongo_data.document_base import Document, db


class Movie(Document):
    collection = db.movies