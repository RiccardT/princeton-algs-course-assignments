from test_utilities.dynamic_test_creator import \
    run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.union_find_with_largest_functionality_test_data import \
    union_find_with_find_largest_functionality_test_data


def union_find_client(n: int, queries: list) -> list:
    """
    maintain an extra array to the weighted quick-union data structure
    that stores for each root {i} the largest element in the connected
    component containing i, called largest[i]
    """
    union_find: UnionFindWithFindLargest = UnionFindWithFindLargest(n)
    results: list = []
    for query in queries:
        if query[0] == "union":
            results.append(union_find.union(query[1], query[2]))
        elif query[0] == "connected":
            results.append(union_find.connected(query[1], query[2]))
        elif query[0] == "find":
            results.append(union_find.find(query[1]))
    return results


class UnionFindWithFindLargest:

    def __init__(self, number_of_nodes: int):
        self.roots: list = [i for i in range(number_of_nodes)]  # O(n)
        self.tree_sizes: list = [1 for _ in range(number_of_nodes)]  # O(n)
        self.largest: list = [i for i in range(number_of_nodes)]  # O(n)

    def find(self, node: int) -> int:  # O(log(n)
        root: int = self.__get_root(node)
        largest_connected_to_node: int = self.largest[root]
        self.largest[node] = largest_connected_to_node
        return largest_connected_to_node

    def connected(self, p: int, q: int) -> bool:  # O(log(n))
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:   # O(log(n))
        root_of_p: int = self.__get_root(p)  # O(log(n))
        root_of_q: int = self.__get_root(q)  # O(log(n))
        self.__update_largest(root_of_p, root_of_q)
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

    def __update_largest(self, root_p: int, root_q: int):
        largest_connected_to_p: int = self.largest[root_p]
        largest_connected_to_q: int = self.largest[root_q]
        if largest_connected_to_p < largest_connected_to_q:
            self.largest[root_p] = largest_connected_to_q
        else:
            self.largest[root_q] = largest_connected_to_p

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print(f"Index: {[index for index in range(len(self.roots))]}")
        print(f"Roots: {self.roots}")
        print(f"Tree Sizes: {self.tree_sizes}")
        print(f"Largest: {self.largest}")

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])


if __name__ == '__main__':
    dynamically_generate_tests(union_find_with_find_largest_functionality_test_data, union_find_client, timed=True)
    run_dynamic_tests()
