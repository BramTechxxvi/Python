from ClassWork.library.author import Author
from random import randint

class Book:

    def __init__(self, title, author: Author):
        self._title = None
        if not isinstance(author, Author): raise ValueError('Author must be an instance of class Author')
        self._author = author
        self._isbn = None
        self._available = False
        self.title = title
        self.generate_isbn()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self.validate_title(value)
        self._title = value.title()

    def validate_title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be alphabets")
        if not value.strip():
            raise ValueError("Title cannot be empty")

    def generate_isbn(self):
        prefix = '973-'
        suffix = ''.join(str(randint(0, 9)) for _ in range(10))
        self._isbn = prefix + suffix