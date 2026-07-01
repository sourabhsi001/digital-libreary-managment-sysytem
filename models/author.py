from models import db

class Author(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(100),nullable=True)
    biography=db.Column(db.Text)
    books = db.relationship("Book", backref="author", lazy=True)