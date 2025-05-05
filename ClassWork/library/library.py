from typing import List

from ClassWork.library.book import Book


class Library:
    def __init__(self):
        self.book = List[Book()]
        self.borrowed_books = {}

    def add_books(self, book: Book):
        self.book.append(book)

    def borrow_book(self):
        self.borrowed_books[Book()] = Book()

    def return_book(self):
        self.borrowed_books[Book()] = Book()

    def view_available_books(self):
        for book in self.borrowed_books.values():
            return f"Available books: {book}\n"


    def view_borrowed_books(self):
        for book in self.borrowed_books.values():
            print(book.title)