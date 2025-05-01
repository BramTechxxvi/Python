class MyStack:

    def __init__(self, size):
        self.data = [size]
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, element):
        if self.top == len(self.data) -1 :
            print("Stack is full")
        else:
            self.data[++self.top] = element

    def is_full(self):
        return self.top == len(self.data) -1


