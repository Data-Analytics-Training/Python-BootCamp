"""
SQLite is a C-language library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.

The SQLite library is in the public domain. As a result, it can be used for any purpose, without restriction.

SQLite is an in-process library. It does not have a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.

"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

cursor.execute("SELECT * FROM books")

books = cursor.fetchall()  # fetches all the data from the table

print(books)
# [(1, 'The Lords of the Rings', 'Tolkien'), (2, 'Python Lessons', 'Sinan URUN')]

for book in books:
  print(f"Book ID: {book[0]}, Book Title: {book[1]}, Authors: {book[2]}")

link.close()
