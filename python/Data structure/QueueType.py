MAX_ITEMS = 100

class QueueType():
    def __init__(self):
        self.info = []

    def enqueue(self, data):
        if len(self.info) == MAX_ITEMS:
            print("already full")
        else:
            self.info.append(data)

    def dequeue(self):
        if len(self.info) == 0:
            print("already empty")
        else:
            item = self.info[0]
            del self.info[0]
            return item

    def is_empty(self):
        if len(self.info) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.info) == MAX_ITEMS:
            return True
        else:
            return False

    def make_empty(self):
        while len(self.info) != 0:
            del self.info[0]