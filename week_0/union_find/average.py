from test_utilities.dynamic_test_creator import run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.functionality_test_data import functionality_test_data


def union_find_client(n: int, queries: list) -> list:
    union_find: UnionFind = UnionFind(n)
    results: list = []
    for query in queries:
        if query[0] == "union":
            results.append(union_find.union(query[1], query[2]))
        elif query[0] == "connected":
            results.append(union_find.connected(query[1], query[2]))
    return results


class UnionFind:

    def __init__(self, number_of_nodes: int):
        self.roots: list = [i for i in range(number_of_nodes)]

    def connected(self, p: int, q: int) -> bool:
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:
        root_of_p: int = self.__get_root(p)
        root_of_q: int = self.__get_root(q)
        self.roots[root_of_p] = root_of_q

    def __get_root(self, node: int):
        while node != self.roots[node]:
            node = self.roots[node]
        return node

    def log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print([index for index in range(len(self.roots))])
        print(self.roots)

    def log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.roots[p] == self.roots[q])


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, union_find_client)
    run_dynamic_tests()
