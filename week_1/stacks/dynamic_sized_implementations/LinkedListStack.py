from week_1.stacks.StackInterface import StackInterface


class LinkedListStack(StackInterface):

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.item
            self.current = self.current.next
            return item

    def push(self, item) -> None:
        old_first: LinkedListStack.Node = self.first
        self.first = self.Node(item)
        self.first.next = old_first
        self.current = self.first

    def pop(self):
        item: LinkedListStack.Node = self.first.item
        self.first = self.first.next
        return item

    def is_empty(self) -> bool:
        return self.first is None

    def size(self) -> int:
        count: int = 0
        traveler: LinkedListStack.Node = self.first
        while next is not None:
            traveler = traveler.next
            count += 1
        return count
