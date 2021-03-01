from typing import Any
from week_1.queues.QueueInterface import QueueInterface


class LinkedListQueue(QueueInterface):

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, element: Any) -> None:
        old_last: LinkedListQueue.Node = self.last
        self.last = LinkedListQueue.Node(element)
        self.last.next = None
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def is_empty(self) -> bool:
        return self.first is None

    def dequeue(self) -> Any:
        item: Any = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item

    def size(self) -> int:
        count: int = 0
        traveler: LinkedListQueue.Node = self.first
        while traveler.next is not None:
            traveler = traveler.next
            count += 1
        return count
