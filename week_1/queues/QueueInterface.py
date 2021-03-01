from typing import Any


class QueueMeta(type):
    """
    A metaclass that will be used for percolation class creation
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'enqueue') and
                callable(subclass.enqueue) and
                hasattr(subclass, 'dequeue') and
                callable(subclass.dequeue) and
                hasattr(subclass, 'is_empty') and
                callable(subclass.is_empty) and
                hasattr(subclass, 'size') and
                callable(subclass.size))


class QueueInterface(metaclass=QueueMeta):

    def enqueue(self, element) -> None:
        pass

    def dequeue(self) -> Any:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass
