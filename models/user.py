from datetime import datetime
from models import db

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    role=db.Column(db.String(100),default="member")
    phone=db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)