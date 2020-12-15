from test_utilities.dynamic_test_creator import run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.union_find_functionality_test_data import union_find_functionality_test_data


def union_find_client(n: int, queries: list) -> list:
    """
    -   Since our trees are now self balancing and the union and connected methods are now
        capped at O(log(n) [i.e. because depth is at most log(n)] then our client
        Will take at worst O(n + queries*log(n)).

    -   With path compression:
        Since our path compression flattens out our trees, we can reduce the time complexity
        of union and find to log(n)*, which in practice is ~= 5, essentially a constant factor!
        Therefore, we can amortize the runtime to be: O(n + queries)
    """
    balanced_union_find: OptimalUnionFind = OptimalUnionFind(n)
    results: list = []
    for query in queries:
        if query[0] == "union":
            results.append(balanced_union_find.union(query[1], query[2]))
        elif query[0] == "connected":
            results.append(balanced_union_find.connected(query[1], query[2]))
    return results


class OptimalUnionFind:

    def __init__(self, number_of_nodes: int):
        self.roots: list = [i for i in range(number_of_nodes)]  # O(n)
        self.tree_sizes: list = [1 for _ in range(number_of_nodes)]  # O(n)

    def connected(self, p: int, q: int) -> bool:  # O(log(n))
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:   # O(log(n))
        root_of_p: int = self.__get_root(p)  # O(log(n))
        root_of_q: int = self.__get_root(q)  # O(log(n))
        if root_of_p == root_of_q:
            return
        if self.tree_sizes[root_of_p] < self.tree_sizes[root_of_q]:  # O(1)
            self.roots[root_of_p] = root_of_q
            self.tree_sizes[root_of_q] += self.tree_sizes[root_of_p]
        else:   # O(1)
            self.roots[root_of_q] = root_of_p
            self.tree_sizes[root_of_p] += self.tree_sizes[root_of_p]

    def __get_root(self, node: int):  # O(log(n))
        while node != self.roots[node]:
            self.__compress_path(node)
            node = self.roots[node]
        return node

    def __compress_path(self, node: int):  # Set node to point to it's grandparent
        self.roots[node] = self.roots[self.roots[node]]

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print([index for index in range(len(self.roots))])
        print(self.roots)

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])


if __name__ == '__main__':
    dynamically_generate_tests(union_find_functionality_test_data, union_find_client, timed=True)
    run_dynamic_tests()
