from typing import List

from week_0.union_find.percolation.interfaces.PercolationInterface import PercolationInterface
from week_0.union_find.OptimalUnionFind import OptimalUnionFind


class Percolation(PercolationInterface):

    def __init__(self, n: int):
        self.__validate_init_input(n)
        self.__n: int = n
        self.__total_normal_sites: int = n ** 2
        total_virtual_sites: int = 2
        self.__union_find: OptimalUnionFind = OptimalUnionFind(self.__total_normal_sites + total_virtual_sites)
        self.__top_virtual_site: int = self.__total_normal_sites
        self.__bottom_virtual_site: int = self.__total_normal_sites + 1
        self.__connect_virtual_site(self.__top_virtual_site)
        self.__connect_virtual_site(self.__bottom_virtual_site)
        self.__opened: List[bool] = [False for _ in range(self.__total_normal_sites)]
        self.__number_of_open_sites: int = 0

    @staticmethod
    def __validate_init_input(n: int):
        if n <= 0:
            Exception(f'Input of n: {n} is invalid, n must be greater than 0')

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

    def open(self, row: int, col: int):
        self.__validate_grid_inputs(row, col)
        u_f_node: int = self.__get_associated_u_f_node(row, col)
        self.__opened[u_f_node] = True
        neighbor_u_f_nodes: List[int] = self.__get_neighbor_u_f_nodes(u_f_node)
        for neighbor_node in neighbor_u_f_nodes:
            if self.__opened[neighbor_node]:
                self.__union_find.union(u_f_node, neighbor_node)
        self.__number_of_open_sites += 1

    def __validate_grid_inputs(self, row: int, col: int):
        if row < 0 or row >= self.__n:
            raise Exception(f'Input of row: {row} out of range, row must be between 0 and {self.__n}')
        elif col < 0 or col >= self.__n:
            raise Exception(f'Input of col: {col} out of range, col must be between 0 and {self.__n}')

    def __get_associated_u_f_node(self, row: int, col: int) -> int:
        return row * self.__n + col

    def __get_neighbor_u_f_nodes(self, node: int) -> List[int]:
        left: int = node - 1
        right: int = node + 1
        up: int = node - self.__n
        down: int = node + self.__n
        potential_neighbors: List[int] = [left, right, up, down]
        actual_neighbors: List[int] = []
        for potential_neighbor in potential_neighbors:
            if potential_neighbor in range(self.__total_normal_sites):
                actual_neighbors.append(potential_neighbor)
        return actual_neighbors

    def is_open(self, row: int, col: int) -> bool:
        self.__validate_grid_inputs(row, col)
        u_f_node: int = self.__get_associated_u_f_node(row, col)
        return self.__opened[u_f_node]

    def is_full(self, row: int, col: int) -> bool:
        self.__validate_grid_inputs(row, col)
        u_f_node: int = self.__get_associated_u_f_node(row, col)
        return self.__opened[u_f_node] and self.__union_find.connected(self.__top_virtual_site, u_f_node)

    def number_of_open_sites(self) -> int:
        return self.__number_of_open_sites

    def percolates(self) -> bool:
        return self.__union_find.connected(self.__top_virtual_site, self.__bottom_virtual_site)
