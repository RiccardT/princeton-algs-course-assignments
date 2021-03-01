from week_1.stacks.StackInterface import StackInterface


class LinkedListStack(StackInterface):

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None

    def push(self, item) -> None:
        old_first: LinkedListStack.Node = self.first
        first = self.Node(item)
        first.next = old_first

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
