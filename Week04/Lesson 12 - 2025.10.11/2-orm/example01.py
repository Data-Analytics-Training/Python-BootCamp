"""
SQLAlchemy

SQLAlchemy, allows you to perform all database operations using Python objects and classes, almost completely eliminating the need to write SQL
manually.
"""

"""
Library Management with SQLAlchemy ORM

1. What is ORM?
ORM (Object-Relational Mapping Operations) means mapping objects to relational data.

Purpose: To create a bridge between the classes and objects you write in Python (object-oriented side) and the tables and rows in a relational
database (relational side).

Benefits: Instead of writing raw SQL commands (such as SELECT, INSERT, UPDATE, DELETE) you can perform database operations as if you were working
with normal Python objects.

This makes your code more secure, readable, and database-independent.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///library_orm.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Book(Base):
  __tablename__ = "books"  # the name of the table to be created in the database

  id = Column(Integer, primary_key=True)
  title = Column(String)
  author = Column(String)

  def __repr__(self):
    return f"Book (id: {self.id}, title= {self.title}, author = {self.author})"


Base.metadata.create_all(engine)

book1 = Book(title="Python Lessons", author="John Dow")

session.add(book1)
session.commit()
