import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserLogin(Base):
    __tablename__ = "usersinfo"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)

class Books(Base):
    __tablename__ = "books"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    title = sql.Column(sql.String, index=True)
    author = sql.Column(sql.String, index=True)
    version = sql.Column(sql.String, index=True)
    isbn = sql.Column(sql.String, index=True)
    count = sql.Column(sql.Integer, index=True)

class RentedBooks(Base):
    __tablename__ = "rentedbooks"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    user_id = sql.Column(sql.Integer, sql.ForeignKey("usersinfo.id"))
    book_id = sql.Column(sql.Integer, sql.ForeignKey("books.id"))
    rented_on = sql.Column(sql.Date)
    returned_on = sql.Column(sql.Date)