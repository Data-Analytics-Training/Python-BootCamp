"""
What is a Database and Why is it Necessary?

What is it?
A database is an organized collection of data.
Just like a library organized its books, databased organize information.

Why is it Necessary?
It is needed to store information permanently - such as user data, product lists, or notes - that we don't want to lose when our program closes.

What is SQLite?
SQLite is a lightweight, serverless database engine that stores the entire database in a single file.
It is very easy to use with Python and requires no installation.
"""

# In python, the standart module sqlite3 is used to database operations.

# To work with a database, we must first establish a connection

import sqlite3

link = sqlite3.connect("library.db")

# * Once a connection is established, we should close it after we are done
link.close()
