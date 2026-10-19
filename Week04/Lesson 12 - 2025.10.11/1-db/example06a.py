"""
Update a book's name in the "books" table using its ID.
"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()


book_id = int(input("Please enter the ID of book to be updated: "))
book_name = input("Please enter the name of the book to be updated: ")

# Update a book's name by its ID
cursor.execute("UPDATE books SET name=? WHERE id=?", (book_name, book_id))

# Commit the changes to the database
link.commit()

link.close()
