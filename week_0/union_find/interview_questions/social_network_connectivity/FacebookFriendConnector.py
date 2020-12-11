

class FacebookFriendConnector:

    def __init__(self, number_of_nodes: int):
        self.roots: list = [i for i in range(number_of_nodes)]  # O(n)
        self.tree_sizes: list = [1 for _ in range(number_of_nodes)]  # O(n)
        self.max_tree_size: int = 1

    def connected(self, p: int, q: int) -> bool:  # O(log(n))
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:   # O(log(n))
        root_of_p: int = self.__get_root(p)  # O(log(n))
        root_of_q: int = self.__get_root(q)  # O(log(n))
        if root_of_p == root_of_q:
            self.__log_union_state(p, q)
            return
        if self.tree_sizes[root_of_p] < self.tree_sizes[root_of_q]:  # O(1)
            self.roots[root_of_p] = root_of_q
            self.tree_sizes[root_of_q] += self.tree_sizes[root_of_p]
            self.__update_max_tree_size(self.tree_sizes[root_of_q])
        else:   # O(1)
            self.roots[root_of_q] = root_of_p
            self.tree_sizes[root_of_p] += self.tree_sizes[root_of_p]
            self.__update_max_tree_size(self.tree_sizes[root_of_p])
        self.__log_union_state(p, q)

    def __get_root(self, node: int):  # O(log(n))
        while node != self.roots[node]:
            self.__compress_path(node)
            node = self.roots[node]
        return node

    def __compress_path(self, node: int):  # Set node to point to it's grandparent
        self.roots[node] = self.roots[self.roots[node]]

    def __update_max_tree_size(self, tree_size: int):
        if tree_size > self.max_tree_size:
            self.max_tree_size = tree_size

    def all_connected(self) -> bool:
        return self.max_tree_size == len(self.roots)

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print(f"Index: {[index for index in range(len(self.roots))]}")
        print(f"Roots: {self.roots}")
        print(f"Tree Sizes: {self.tree_sizes}")

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])