class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None

class CircularLL:
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

    def find_item(self, listData, item):
        if self.length == 0:
            return False
        else:
            if self.listData.info == item:
                return True
            else:
                location = self.listData.next
                while location != self.listData:
                    if location.info == item:
                        return True
                    else:
                        location = location.next
                return False

    def insert_item(self, item):
        node = NodeType(item)
        if self.length == 0:
            self.listData = node
            node.next = self.listData
        else:
            location = self.listData
            predLoc = None
            while predLoc != location:
                if location.info < item:
                    predLoc = location
                    location = location.next
                else:
                    break
            if predLoc == None:
                node.next = self.listData.next
                self.listData.next = node
            else:
                node.next = location
                predLoc.next = node
                self.listData = node
        self.length += 1

    def delete_item(self, item):
        if self.find_item(0, item):
            location = self.listData.next
            predLoc = self.listData
            if self.listData.info == item:
                while location.next != self.listData:
                    location = location.next
                temp_location = self.listData
                location.next = self.listData.next
                self.listData = location
                del temp_location
                self.length -= 1
            else:
                while True:
                    if location.info == item:
                        predLoc.next = location.next
                        del location
                        self.length -= 1
                        break
                    else:
                        predLoc = location
                        location = location.next

    def reset_list(self):
        self.currentPos = None

    def get_next_item(self):
        if self.currentPos == None:
            self.currentPos = self.listData
        else:
            self.currentPos = self.currentPos.next
        return self.currentPos.info

    def __str__(self):
        self.reset_list()
        items = []
        for i in range(0, self.length):
            t = self.get_next_item()
            items.append(str(t))
        return " ".join(items)
