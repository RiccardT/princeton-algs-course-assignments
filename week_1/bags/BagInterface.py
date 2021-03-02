from typing import Any


class BagMeta(type):
    """
    A metaclass that will be used for percolation class creation
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'add') and
                callable(subclass.add) and
                hasattr(subclass, 'size') and
                callable(subclass.size) and
                hasattr(subclass, '__iter__') and
                callable(subclass.__iter__))


class BagInterface(metaclass=BagMeta):

    def add(self, item) -> None:
        pass

    def size(self) -> int:
        pass

    def __iter__(self) -> Any:
        pass