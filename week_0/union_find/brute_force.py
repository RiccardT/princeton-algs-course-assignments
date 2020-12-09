from test_utilities.dynamic_test_creator import run_dynamic_tests, dynamically_generate_tests
from week_0.union_find.test_resources.union_find_functionality_test_data import union_find_functionality_test_data


def union_find_client(n: int, queries: list) -> list:
    """
    O(N + queries*N) -> O(queries*N) -> O(N*2) for N union commands on N entries
    """
    union_find: UnionFind = UnionFind(n)  # O(N)
    results: list = []
    for query in queries:  # O(queries * N)
        if query[0] == "union":
            results.append(union_find.union(query[1], query[2]))  # O(N)
        elif query[0] == "connected":
            results.append(union_find.connected(query[1], query[2]))  # O(1)
    return results


class UnionFind:

    def __init__(self, entries: int):
        self.ids: list = [id for id in range(entries)]  # O(N)

    def connected(self, p: int, q: int) -> bool:  # O(1)
        self.__log_connected_state(p, q)
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int) -> None:   # O(N)
        p_id: int = self.ids[p]
        q_id: int = self.ids[q]
        for entry, id in enumerate(self.ids):
            if id == p_id:
                self.ids[entry] = q_id
        self.__log_union_state(p, q)

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print([index for index in range(len(self.ids))])
        print(self.ids)

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self.ids[p] == self.ids[q])


if __name__ == '__main__':
    dynamically_generate_tests(union_find_functionality_test_data, union_find_client)
    run_dynamic_tests()
