

class PercolationInterface:

    def __init__(self, n: int) -> None:
        """
        Creates an nxn grid, with all sites initially blocked
        """
        pass

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
