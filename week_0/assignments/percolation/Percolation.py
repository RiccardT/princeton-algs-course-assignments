from week_0.assignments.percolation.interfaces.PercolationInterface import PercolationInterface
from week_0.union_find.OptimalUnionFind import OptimalUnionFind


class Percolation(PercolationInterface):

    def __init__(self, n: int):
        self.unionFind: OptimalUnionFind = OptimalUnionFind(n)

    def open(self, row: int, col: int):
        pass

    def is_open(self, row: int, col: int) -> bool:
        return False

    def is_full(self, row: int, col: int) -> bool:
        return False

    def number_of_open_sites(self) -> int:
        return 0

    def percolates(self) -> bool:
        return False

