

class PercolationMeta(type):
    """
    A metaclass that will be used for percolation class creation
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'open') and
                callable(subclass.open) and
                hasattr(subclass, 'is_open') and
                callable(subclass.is_open) and
                hasattr(subclass, 'is_full') and
                callable(subclass.is_full) and
                hasattr(subclass, 'number_of_open_sites') and
                callable(subclass.number_of_open_sites) and
                hasattr(subclass, 'percolates') and
                callable(subclass.percolates))


class PercolationInterface(metaclass=PercolationMeta):

    def open(self, row: int, col: int) -> None:
        """
        Opens the site (row, col) if it is not open already
        """
        pass

    def is_open(self, row: int, col: int) -> bool:
        pass

    def is_full(self, row: int, col: int) -> bool:
        pass

    def number_of_open_sites(self) -> int:
        pass

    def percolates(self) -> bool:
        pass
