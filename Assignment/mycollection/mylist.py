class MyList:

    def __init__(self):
        self.items = []

    def add_element(self, element):
        self.items.(element)
        return element

    def remove_element(self, element):
        if element not in self.items:
            return None
        self.items.remove(element)
        return element

    def extend_element(self, elements):
        self.items.extend(elements)
        return elements

    def clear_element(self):
        self.items.clear()
        return True

    def count_element(self, element):
        return self.items.count(element)

    def copy_element(self, element):
        return self.items.copy()

    def get_index_of_element(self, element):
        try:
            return self.items.index(element)
        except ValueError:
            return None

    def insert_element(self, index, element):
        self.items.insert(index, element)
        return element

    def sort_element(self, reverse=False):
        self.items.sort(reverse=reverse)
        return self.items

    def reverse_element(self):
        self.items.reverse()
        return self.items

    def pop_element(self, element):
        pass