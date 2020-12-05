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

    def __init__(self, entries: int):
        self.ids: list = [id for id in range(entries)]

    def connected(self, p: int, q: int) -> bool:
        print(f"connected({p}, {q})")
        print(self.ids[p] == self.ids[q])
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int) -> None:
        p_id: int = self.ids[p]
        q_id: int = self.ids[q]
        entries_that_match_p: list = []
        for entry, id in enumerate(self.ids):
            if id == p_id:
                entries_that_match_p.append(entry)
        for entry in entries_that_match_p:
            self.ids[entry] = q_id
        print(f"union({p}, {q})")
        print([index for index in range(len(self.ids))])
        print(self.ids)
        print(entries_that_match_p)


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, union_find_client)
    run_dynamic_tests()
