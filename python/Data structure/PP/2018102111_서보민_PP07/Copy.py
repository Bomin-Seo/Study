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
            print("Failed to Push")
        else:
            location = NodeType(item)
            location.next = self.topPtr
            self.topPtr = location

    def pop(self):
        if self.is_empty():
            print("Failed to Pop")
        else:
            tempPtr = self.topPtr.info
            self.topPtr = self.topPtr.next
            return tempPtr

    def top(self):
        if self.is_empty():
            print("Failed to Top")
        else:
            return self.topPtr.info

    def __str__ (self):

        location = self.topPtr
        items = []
        while location != None:
            items.append(location.info)
            location = location.next

        return " ".join(items)

    def copy(self, anotherStack):
        if anotherStack.topPtr == None:
            self.topPtr = None
        else:
            self.topPtr = NodeType(anotherStack.topPtr.info)
            ptr1 = anotherStack.topPtr.next
            ptr2 = self.topPtr
            while ptr1 != None:
                ptr2.next = NodeType(ptr1.info)
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            ptr2.next = None

            
            
        
            





