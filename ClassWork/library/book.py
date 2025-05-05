from ClassWork.library.author import Author
from random import randint

class Book:

    def __init__(self):
        self.title = str
        self.author = Author(first_name=)
        self.isbn = str
        self.available = True

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self.title = value.title()

    def generate_isbn(self):
        prefix = '973-'
        suffix = ''.join(str(randint(0, 9)) for _ in range(10))
        self.isbn = prefix + suffix

    def validate_title(self, value):
        if value is not type(str): raise ValueError("Title must be alphabets")
        if "" == value == " ": raise ValueError("Title cannot be empty")
