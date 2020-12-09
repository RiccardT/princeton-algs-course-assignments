from test_utilities.dynamic_test_creator import run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.union_find_functionality_test_data import union_find_functionality_test_data


def union_find_client(n: int, queries: list) -> list:
    """
    - Total Time Complexity:
        O(number_of_unions*n + number_of_connecteds*n) -> O(n[unions + connecteds])
        ~= O(n^2) for n connecteds and/or union queries
    - This occurs at worst when we have large, skinny trees, where depth of the tree is n nodes
    """
    union_find: UnionFind = UnionFind(n)
    results: list = []
    for query in queries:
        if query[0] == "union":
            results.append(union_find.union(query[1], query[2]))
        elif query[0] == "connected":
            results.append(union_find.connected(query[1], query[2]))
    return results


class UnionFind:

    def __init__(self, number_of_nodes: int):  # O(n)
        self.roots: list = [i for i in range(number_of_nodes)]

    def connected(self, p: int, q: int) -> bool:  # O(n)
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:  # O(n)
        root_of_p: int = self.__get_root(p)
        root_of_q: int = self.__get_root(q)
        self.roots[root_of_p] = root_of_q

    def __get_root(self, node: int):  # O(n)
        while node != self.roots[node]:
            node = self.roots[node]
        return node

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print([index for index in range(len(self.roots))])
        print(self.roots)

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])


if __name__ == '__main__':
    dynamically_generate_tests(union_find_functionality_test_data, union_find_client)
    run_dynamic_tests()
