""" """

import sqlite3

link = sqlite3.connect("library.db")

cursor = link.cursor()

cursor.execute("DELETE FROM books WHERE id =?", (1,))

link.commit()

link.close()
