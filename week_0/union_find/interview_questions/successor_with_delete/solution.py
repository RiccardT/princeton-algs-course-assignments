from test_utilities.dynamic_test_creator import \
    run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.union_find_with_successor_and_delete_functionality_test_data import \
    union_find_with_successor_and_delete_functionality_test_data


def successor_with_delete_client(n: int, queries: list) -> list:
    """
    - remove(x)
        This corresponds to union(x, x + 1)
    - successor(x)
        this corresponds to getting the successor_roots[get_root(x + 1)]
    """
    union_find_with_successor_and_delete: UnionFindWithRemoveAndSuccessor = UnionFindWithRemoveAndSuccessor(n)
    results: list = []
    for query in queries:
        if query[0] == "remove":
            results.append(union_find_with_successor_and_delete.remove(query[1]))
        elif query[0] == "successor":
            results.append(union_find_with_successor_and_delete.successor(query[1]))
    return results


class UnionFindWithRemoveAndSuccessor:

    def __init__(self, number_of_nodes: int):
        self.roots: list = [i for i in range(number_of_nodes)]  # O(n)
        self.tree_sizes: list = [1 for _ in range(number_of_nodes)]  # O(n)
        self.successor_roots: list = [i for i in range(number_of_nodes)]  # O(n)

    def remove(self, x: int):
        self.__union(x, x + 1)

    def successor(self, x: int):
        return self.successor_roots[self.__get_root(x + 1)]

    def __connected(self, p: int, q: int) -> bool:  # O(log(n))
        return self.__get_root(p) == self.__get_root(q)

    def __union(self, p: int, q: int) -> None:   # O(log(n))
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

            self.successor_roots[root_of_p] = self.successor_roots[root_of_q]  # Successor mod

    def __get_root(self, node: int):  # O(log(n))
        while node != self.roots[node]:
            self.__compress_path(node)
            node = self.roots[node]
        return node

    def __compress_path(self, node: int):  # Set node to point to it's grandparent
        self.roots[node] = self.roots[self.roots[node]]

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print(f"Index: {[index for index in range(len(self.roots))]}")
        print(f"Roots: {self.roots}")
        print(f"Tree Sizes: {self.tree_sizes}")

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])


if __name__ == '__main__':
    dynamically_generate_tests(
        union_find_with_successor_and_delete_functionality_test_data, successor_with_delete_client, timed=True)
    run_dynamic_tests()
