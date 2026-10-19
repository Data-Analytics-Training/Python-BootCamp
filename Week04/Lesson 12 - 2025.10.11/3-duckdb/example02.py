from dataclasses import dataclass

import duckdb

conn = duckdb.connect('library_duckdb.db')

@dataclass
class Book:
    id: int
    title: str
    author: str

def fetch_books(query: str, params: list | None = None) -> list[Book]:
    rows = conn.execute(query, params or []).fetchall()
    return [Book(*row) for row in rows]

# Sequence + Table
conn.execute("CREATE SEQUENCE IF NOT EXISTS book_id_seq START 1")
conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY DEFAULT nextval('book_id_seq'),
        title VARCHAR,
        author VARCHAR
    )
    """)

# List All
all_books = fetch_books("SELECT id, title, author FROM books")
print(type(all_books), all_books)

for book in all_books:
    print(book.title)


# Filtering
filtered = fetch_books(
    "SELECT id, title, author FROM books WHERE author=?", ['John DOE']
)

print(f'Filtered Books: {filtered}')

# Updating
conn.execute("UPDATE books SET title = ? WHERE id = ?", ["Python Bootcamp Lessons", 1])

all_books = fetch_books("SELECT id, title, author FROM books")
for book in all_books:
    print(book.title)

# Deleting
conn.execute("DELETE FROM books WHERE id = ?", [2])

print(fetch_books("SELECT id, title, author FROM books"))
