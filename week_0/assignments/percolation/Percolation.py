from typing import List

from week_0.assignments.percolation.interfaces.PercolationInterface import PercolationInterface
from week_0.union_find.OptimalUnionFind import OptimalUnionFind


class Percolation(PercolationInterface):

    def __init__(self, n: int):
        self.__n: int = n
        self.__total_normal_sites: int = n ** 2
        total_virtual_sites: int = 2
        self.__union_find: OptimalUnionFind = OptimalUnionFind(self.__total_normal_sites + total_virtual_sites)
        self.__top_virtual_site: int = self.__total_normal_sites
        self.__bottom_virtual_site: int = self.__total_normal_sites + 1
        self.__connect_virtual_site(self.__top_virtual_site)
        self.__connect_virtual_site(self.__bottom_virtual_site)
        self.__opened: List[List[bool]] = [
            [False for _ in range(n)] for _ in range(n)
        ]

    def open(self, row: int, col: int):
        self.__opened[col][row] = True
        u_f_node: int = self.__get_associated_u_f_node(row, col)
        adjacent_u_f_nodes: List[int] = self.__get_adjacent_u_f_nodes(row, col)
        # TODO: Figure out how to fully go from the union find node paradigm to the percolation matrix paradigm and back

    def __get_associated_u_f_node(self, row: int, col: int) -> int:
        return row * self.__n + col

    def __get_adjacent_u_f_nodes(self, row: int, col: int) -> List[int]:
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
        sites_to_be_connected: List[int]
        if virtual_site == self.__top_virtual_site:
            sites_to_be_connected = [
                site for site in range(0, self.__n)
            ]
        else:
            sites_to_be_connected = [
                site for site in range(self.__n * (self.__n - 1), self.__total_normal_sites)
            ]
        for site in sites_to_be_connected:
            self.__union_find.union(virtual_site, site)

