from models import db

class Reseravation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    book_id=db.Column(
        db.Integer,
        db.ForeignKey("book.id"),
        nullable=False
    )
    reservation_date = db.Column(db.Date, nullable=False)

    status = db.Column(
        db.String(20),
        default="Pending"
    )