MAX_ITEMS = 100

empty_str = "Stack is Empty"
full_str = "Stack is Full"

class StackType:
    def __init__(self):
        self.info = []

    def is_empty(self):
        return len(self.info) == 0
        
    def is_full(self):
        return len(self.info) == MAX_ITEMS
        
    def push(self, item):
        if len(self.info) == MAX_ITEMS:
            return full_str
        else:
            self.info.append(item)

    def pop(self):
        if len(self.info) == 0:
            return empty_str
        else:
            del self.info[-1]

    def top(self):
        if len(self.info) == 0:
            return empty_str
        else:
            top_elem = self.info[-1]
            return top_elem
