"""
Multiple Records Insertion in SQLAlchemy ORM

In this example, we will demonstrate how to insert multiple records into a table using SQLAlchemy ORM. We'll create a `Book` class that maps to a "books" table and then use the session to add multiple instances of this class to the database.

The steps are as follows:
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


book2 = Book(title="C++ Lessons", author="Jack Black")
book3 = Book(title="Dart Lessons", author="Jim Carol")

session.add_all([book2, book3])
session.commit()


#  Printing the books added to the database.
all_books = session.query(Book).all()
print(type(all_books), all_books)


for book in all_books:
    print(book.title)

# Filtering
filtered_books = session.query(Book).filter(Book.author == "Jack Black").all()
print(f"Filtered Books: {filtered_books}")

# Updating
updated_book = session.query(Book).filter(Book.id == 1).first()
updated_book.title = "Python Bootcamp Lessons"

session.commit()

# Deleting
deleted_books = session.query(Book).filter(Book.id == 3).first()
session.delete(deleted_books)
session.commit()

books = session.query(Book).all()
print(books)
