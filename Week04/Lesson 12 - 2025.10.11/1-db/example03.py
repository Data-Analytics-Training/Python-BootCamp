"""
We are going to create a database for our library. The database will have one table called "books". This table will have three columns: id, name and author.

The id column is an integer that will be auto-incremented every time we add a new book. The name and author columns are text fields where
"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  author TEXT
  )
  """)

# We need to commit on order to save the changes made
link.commit()

link.close()
print("Database created successfully! :)")
