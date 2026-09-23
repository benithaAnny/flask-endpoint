class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("cannot pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
