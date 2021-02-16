from .db import db


class Counter(db.Document):
    name = db.StringField(required=True, unique=True)
    counter = db.IntField()
