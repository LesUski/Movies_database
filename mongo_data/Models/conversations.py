from mongo_data.document_base import Document, db


class Conversation(Document):
    collection = db.conversations
