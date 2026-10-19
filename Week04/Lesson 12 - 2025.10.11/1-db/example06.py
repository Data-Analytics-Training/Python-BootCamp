"""
Update a book's name in the "books" table using its ID.
"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

# Update a book's name by its ID
cursor.execute("UPDATE books SET name=? WHERE id=?", ("Hobbit", 1))

# Commit the changes to the database
link.commit()

link.close()
