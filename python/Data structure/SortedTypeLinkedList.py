class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class SortedType:
    def __init__(self):
        self.listData = None
        self.length = 0
        self.currentPos = None

    def is_full(self):
        try:
            location = NodeType("test")
            return False
        except:
            return True

    def length_is(self):
        return self.length

    def make_empty(self):
        while self.listData != None:
            tempPtr = self.listData.next
            del self.listData
            self.listData = tempPtr
        self.length = 0

    def retrieve_item(self, item):
        location = self.listData
        found = False
        moreToSearch = location != None

        while moreToSearch and not found:
            if location.info < item:
                location = location.next
                moreToSearch = location != None
            elif location.info == item:
                found = True
            else:
                moreToSearch = False

        return found

    def insert_item(self, item):
        location = self.listData
        predLoc = None
        moreToSearch = location != None
        while(moreToSearch):
            if location.info < item:
                predLoc = location
                location = location.next
                moreToSearch = location != None
            else:
                moreToSearch = False
        node = NodeType(item)
        if predLoc == None:
            node.next = self.listData
            self.listData = node
        else:
            node.next = location
            predLoc.next = node
        self.length += 1

    def delete_item(self, item):
        location = self.listData
        templocation = NodeType(item)
        if item == self.listData.info:
            templocation = location
            self.listData = self.listData.next

        else:
            while item != location.next.info:
                location = location.next
            templocation = location.next
            location.next = location.next.next
        del templocation
        self.length -= 1

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        item = self.currentPos.info
        self.currentPos = self.currentPos.next

        return item

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
