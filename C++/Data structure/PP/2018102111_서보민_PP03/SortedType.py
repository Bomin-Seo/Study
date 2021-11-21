from enum import Enum

MAX_ITEMS = 100

class Compare(Enum):
    LESS = 0
    GREATER = 1
    EQUAL = 2
    
class ItemType:
    """ Item Type """

    def __init__(self, val):
        self.val = val

    def compared_to(self, otherItem):
        if self.val < otherItem.val:
            return Compare.LESS
        elif self.val > otherItem.val:
            return Compare.GREATER
        return Compare.EQUAL
    
    def __str__(self):
        return str(self.val)

class SortedType:
    """ Chapter 3: Sorted List """

    def __init__(self):
        self.length = 0
        self.info = []
        self.current_pos = -1

    def make_empty(self):
        self.length = 0

    def length_is(self):
        return self.length

    def is_full(self):
        if self.length == MAX_ITEMS:
            return True
        return False

    def insert_item(self, item):
        item = item.val
        self.info.append(item)
        self.info.sort()
        self.length += 1

    def retrieve_item(self, item): # Binary Search
        item = item.val
        first = 0
        last = self.length - 1
        midpoint = int((first+last)/2)
        while first <= last:
            if item == self.info[midpoint]:
                return True
            elif item < self.info[midpoint]:
                last = midpoint - 1
                midpoint = int((first+last)/2)
            else:
                first = midpoint + 1
                midpoint = int((first+last)/2)

    def delete_item(self, item):
        item = item.val
        first = 0
        last = self.length - 1
        midpoint = int((first+last)/2)
        while first <= last:
            if item == self.info[midpoint]:
                del self.info[midpoint]
                self.length -= 1
                break
            elif item < self.info[midpoint]:
                last = midpoint - 1
                midpoint = int((first+last)/2)
            else:
                first = midpoint + 1
                midpoint = int((first+last)/2)

    def reset_list(self):
        self.current_pos = -1

    def get_next_item(self):
        self.current_pos += 1
        return self.info[self.current_pos]

    def __str__(self):
        self.reset_list()
        print_list = []
        for i in range(self.length):
            print_list.append(str(self.get_next_item()))
        return str(" ".join(print_list))