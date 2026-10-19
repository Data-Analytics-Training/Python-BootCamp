# Replacing SQLAlchemy operations in the orm folder with the DuckDB library

import duckdb

# Create a DuckDB connection (if you want to keep it in memory, use ':memory:')
conn = duckdb.connect("library_duckdb.db")


try:
    # Create a squence for id
    conn.execute("CREATE SEQUENCE seq_book_id")

    # Create a table
    conn.execute("""
        CREATE TABLE books (
        id INTEGER PRIMARY KEY DEFAULT nextval('seq_book_id'),
        title VARCHAR,
        author VARCHAR
        )
        """)

    """
    DuckDB's greatest strength is its ability to directly convert Pandas DataFrames or CSV files into tables.

    You can import a CSV into the database in a single line bu using
    conn.execute("CREATE TABLE books AS SELECT * FROM 'students.csv'")
    """

except duckdb.CatalogException as error:
    print("Database Error: ", error, "\n")

# Insert a row
book_data = ("Python Lessons", "John DOE")
conn.execute("INSERT INTO books VALUES (DEFAULT, ?, ?)", book_data)

# To fecth all data from the database
# print(conn.execute("SELECT * FROM books").fetchall())

books = conn.execute("SELECT * FROM books").fetchall()

for book in books:
    print(f"Book ID: {book[0]}, Book Title: {book[1]}, Authors: {book[2]}")

conn.close()
