# Library System — Full CRUD library manager with SQLite database
import sqlite3

class Library:
    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT
            )
        """)
        self.conn.commit()

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        self.cursor.execute("INSERT INTO books(title, author) VALUES(?, ?)", (title, author))
        self.conn.commit()
        print("Book added.")

    def remove_book(self):
        title = input("Enter title to remove: ")
        self.cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        if self.cursor.fetchall():
            self.cursor.execute("DELETE FROM books WHERE title = ?", (title,))
            self.conn.commit()
            print("Book removed.")
        else:
            print("Book not found.")

    def search_book(self):
        title = input("Enter title to search: ")
        self.cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        data = self.cursor.fetchall()
        if data:
            print("Book found:", data)
        else:
            print("Book not found.")

    def update_author(self):
        title = input("Enter title: ")
        author = input("Enter new author: ")
        self.cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        if self.cursor.fetchall():
            self.cursor.execute("UPDATE books SET author = ? WHERE title = ?", (author, title))
            self.conn.commit()
            print("Author updated.")
        else:
            print("Book not found.")

    def show_all(self):
        self.cursor.execute("SELECT * FROM books")
        data = self.cursor.fetchall()
        if data:
            for book in data:
                print(book)
        else:
            print("No books in library.")

    def close(self):
        self.conn.close()

library = Library()
while True:
    print("1. Add book")
    print("2. Search book")
    print("3. Remove book")
    print("4. Show all")
    print("5. Update author")
    print("6. Quit")
    n = input("---: ")

    if n == "1":
        library.add_book()
    elif n == "2":
        library.search_book()
    elif n == "3":
        library.remove_book()
    elif n == "4":
        library.show_all()
    elif n == "5":
        library.update_author()
    elif n == "6":
        break

library.close()