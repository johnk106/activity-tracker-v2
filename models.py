from . import db
from sqlalchemy.sql import func
from datetime import datetime


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True,
                   nullable=False, autoincrement=True)
    book_name = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    theme = db.Column(db.String(1000))
    pub_year = db.Column(db.String(4))
    is_read = db.Column(db.Boolean)
    date_added = db.Column(db.String(100), nullable=False,
                           default=str(datetime.now()).split(".")[0])
