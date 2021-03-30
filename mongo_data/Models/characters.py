from mongo_data.document_base import Document, db


class Character(Document):
    collection = db.characters