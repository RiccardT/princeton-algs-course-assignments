from week_0.assignments.percolation.interfaces.PercolationInterface import PercolationInterface
from week_0.union_find.OptimalUnionFind import OptimalUnionFind


class Percolation(PercolationInterface):

    def __init__(self, n: int):
        self.dimension: int = n
        self.total_normal_sites: int = n ** 2
        total_virtual_sites: int = 2
        self.union_find: OptimalUnionFind = OptimalUnionFind(self.total_normal_sites + total_virtual_sites)
        self.top_virtual_site: int = self.total_normal_sites
        self.bottom_virtual_site: int = self.total_normal_sites + 1
        self.__connect_virtual_site(self.top_virtual_site)
        self.__connect_virtual_site(self.bottom_virtual_site)

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

    def __connect_virtual_site(self, virtual_site: int):  # O(n*log(n))
        sites_to_be_connected: list
        if virtual_site == self.top_virtual_site:
            sites_to_be_connected = [
                site for site in range(0, self.dimension)
            ]
        else:
            sites_to_be_connected = [
                site for site in range(self.dimension * (self.dimension - 1), self.total_normal_sites)
            ]
        for site in sites_to_be_connected:
            self.union_find.union(virtual_site, site)

