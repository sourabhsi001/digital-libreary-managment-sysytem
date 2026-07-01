from models import db


class Fine(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    loan_id = db.Column(
        db.Integer,
        db.ForeignKey("loan.id"),
        nullable=False
    )

    amount = db.Column(db.Numeric(10, 2), nullable=False)

    paid = db.Column(db.Boolean, default=False)