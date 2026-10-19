""" """

import sqlite3


def list_books():
  link = sqlite3.connect("library.db")
  cursor = link.cursor()

  cursor.execute("SELECT * FROM books")

  books = cursor.fetchall()

  for book in books:
    print(f"Book ID: {book[0]}, Book Title: {book[1]}, Author: {book[2]}")

  if len(books) > 0:
    return True
  else:
    print("No books found to list")
    return False


def add_book():
  link = sqlite3.connect("library.db")
  cursor = link.cursor()

  book_name = input("Enter the book title: ")
  author_name = input("Enter the author's name: ")

  cursor.execute("INSERT INTO books VALUES(NULL, ?,?)", (book_name, author_name))
  link.commit()
  link.close()

  print(f"{book_name} by {author_name} has been added to database.")


def update_book():
  list_info = list_books()

  if list_info:
    link = sqlite3.connect("library.db")
    cursor = link.cursor()

    book_id = int(input("Please enter the ID of book to be updated: "))
    book_name = input("Please enter the name of the book to be updated: ")

    cursor.execute("UPDATE books SET name=? WHERE id=?", (book_name, book_id))

    link.commit()
    link.close()
    print("Book has been updated successfully.")
  else:
    print("No books available for updating.")


def delete_book():
  list_info = list_books()

  if list_info:
    link = sqlite3.connect("library.db")
    cursor = link.cursor()

    book_id = int(input("Please enter the ID of book to be deleted: "))

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    link.commit()
    link.close()
    print("Book has been deleted successfully.")
  else:
    print("No books available for deletion. Please add a book first.")


def program():
  while True:
    print(
      "Welcome to Library Database"
      "\nPlease select the operation you would like to perform:"
      "\n1- List the books"
      "\n2- Add a book"
      "\n3- Update a book"
      "\n4- Delete a book"
      "\n5- Exit"
    )

    option = int(input("Please enter your choise: "))

    match option:
      case 1:
        list_books()
      case 2:
        add_book()
      case 3:
        update_book()
      case 4:
        delete_book()
      case 5:
        break
      case _:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
  program()
