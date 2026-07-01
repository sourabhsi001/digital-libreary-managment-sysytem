from models import db


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    book_id = db.Column(
        db.Integer,
        db.ForeignKey("book.id"),
        nullable=False
    )

    issue_date = db.Column(db.Date, nullable=False)

    due_date = db.Column(db.Date, nullable=False)

    return_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Issued")