from week_1.bags.BagInterface import BagInterface


class ArrayBag(BagInterface):

    def __init__(self):
        self.collection = list()

    def add(self, item):
        self.collection.append(item)

    def size(self):
        return len(self.collection)

    def __iter__(self):
        return iter(self.collection)