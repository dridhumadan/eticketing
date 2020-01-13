from mongoengine import Document, EmbeddedDocument, IntField, ObjectIdField, StringField, EmbeddedDocumentField


class Shows(EmbeddedDocument):
    slot1 = IntField()
    slot2 = IntField()


class Movie(Document):
    movie_id = IntField()
    title = StringField()
    language = StringField()
    rating = StringField()
    description = StringField()
    shows = EmbeddedDocumentField(Shows)


class Booking(Document):
    booking_id = IntField()
    phoneno = IntField()
    movie_id = IntField()
    slot = IntField()
    tickets = IntField()
