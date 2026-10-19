"""

SQLite database operations

"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

book_name = input("Please enter book name: ")
author_name = input("Please enter author's name: ")


cursor.execute("INSERT INTO books VALUES(NULL, ?,?)", (book_name, author_name))

link.commit()
print(f"{book_name} by {author_name} added successfully")

link.close()
