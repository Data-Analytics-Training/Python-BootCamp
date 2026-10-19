"""
Basic Database Operations

In general, we can perform four main operations on databases.
CRUD (Create, Read, Update, Delete) represents the four fundamental operations of a database application.

Operation           Meaning                 SQLCommand
Create              Add data                INSERT
Read                Retrieve data           SELECT
Update              Update data             UPDATE
Delete              Delete data             DELETE
"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

# Inserting new data
cursor.execute("INSERT INTO books VALUES(NULL, ?,?)", ("The Lords of the Rings", "Tolkien"))

link.commit()
link.close()
