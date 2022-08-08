MAX_ITEMS = 10

class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class StackType:
    def __init__(self):
        self.topPtr = None

    def is_full(self):
        try:
            location = NodeType("test")
            del location
            return False
        except:
            return True

    def is_empty(self):
        return self.topPtr == None

    def push(self, item):
        if self.is_full():
            print("Stack is Full")
        else:
            location = NodeType(item)
            location.next = self.topPtr
            self.topPtr = location

    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            tempPtr = self.topPtr
            item = self.topPtr.info
            self.topPtr = self.topPtr.next
            del tempPtr
            return item

    def top(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            return self.topPtr.info

    def __str__(self):
        location = self.topPtr
        while location != None:
            print(location.info, end=" ")
            location = location.next
