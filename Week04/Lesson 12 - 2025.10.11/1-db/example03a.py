import sqlite3

link = sqlite3.connect("library.db")

try:
    cursor = link.cursor()

    cursor.execute("""
      CREATE TABLE books (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      author TEXT
      )
      """)

    # We need to commit on order to save the changes made
    link.commit()
    print("Database created successfully! :)")

except sqlite3.OperationalError as error:
    print("Error: ", error)

finally:
    link.close()
    print("Database closed successfully! :)")
