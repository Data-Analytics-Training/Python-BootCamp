"""
In order to perform operations on a database, we need a cursor
"""

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()  # Cursor has been created
"""
Queries are executed here

"""

# Connection closed (important step)
link.close()
