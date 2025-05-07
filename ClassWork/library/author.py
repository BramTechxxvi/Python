class Author:

    def __init__(self, first_name, last_name, dob):
        self._first_name = None
        self._last_name = None
        self._dob = dob
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if not isinstance(name, str): raise ValueError('First name must be a string')
        if not name.strip(): raise ValueError("Can't be empty")
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        if not isinstance(name, str): raise ValueError('Last name must be a string')
        if not name.strip(): raise ValueError("Can't be empty")
        self._last_name = name
