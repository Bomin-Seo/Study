class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):
        location = self.head
        if location.next == None:
            return False
        else:
            location = location.next
            while location != None:
                if location.info == item:
                    return True
                else:
                    location = location.next
            return False

    def insert_item(self, item, new):
        location = self.head
        while location.info != item:
            location = location.next
        newnode = NodeType(new)
        location.next = newnode
        newnode.back = location

    def delete_item(self, item):
        if self.find_item(item) == True:
            location = self.head
            while location.info != item:
                location = location.next
            if location.next == None:
                (location.back).next = None
            else:
                (location.back).next = location.next
                (location.next).back = location.back
            del location
            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

