from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.user import user
from models.author import Author
from models.book import Book
from models.loan import Loan
from models.reseervation import Reseravation
from models.fine import Fine