from models import db


class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    publisher = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    category = db.Column(db.String(100))
    total_copies = db.Column(db.Integer, default=1)
    available_copies = db.Column(db.Integer, default=1)
    cover_image = db.Column(db.String(255))
    ebook = db.Column(db.String(255))

    author_id = db.Column(
        db.Integer,
        db.ForeignKey("author.id"),
        nullable=False
    )