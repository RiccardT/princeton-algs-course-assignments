from week_1.stacks.StackInterface import StackInterface


class FixedCapacityArrayStack(StackInterface):

    def __init__(self, capacity: int):
        self.n: int = 0
        self.capacity: int = capacity
        self.stack: list = [None] * capacity

    def push(self, element) -> None:
        self.stack[self.n] = element
        self.n += 1

    def pop(self):
        popped_element = self.stack[self.n]
        self.n -= 1
        return popped_element

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n
