

class StackMeta(type):
    """
    A metaclass that will be used for percolation class creation
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'push') and
                callable(subclass.push) and
                hasattr(subclass, 'pop') and
                callable(subclass.pop) and
                hasattr(subclass, 'is_empty') and
                callable(subclass.is_empty) and
                hasattr(subclass, 'size') and
                callable(subclass.size))


class StackInterface(metaclass=StackMeta):

    def push(self, element) -> None:
        pass

    def pop(self):
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass
