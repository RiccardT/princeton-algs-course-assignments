from week_1.stacks.StackInterface import StackInterface


class FixedCapacityArrayStack(StackInterface):

    def __init__(self):
        self.n: int = 0
        self.stack: list = []

    def push(self, element) -> None:
        if self.n == len(self.stack):
            self.__resize(2 * len(self.stack))
        self.stack[self.n] = element
        self.n += 1

    def pop(self):
        popped_element = self.stack[self.n]
        self.n -= 1
        self.stack[self.n] = None
        if self.n > 0 and self.n == len(self.stack) // 4:
            self.__resize(len(self.stack) // 2)
        return popped_element

    def __resize(self, capacity: int):
        copy: list = [0] * capacity
        for i in range(self.n):
            copy[i] = self.stack[i]
        self.stack = copy

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n
