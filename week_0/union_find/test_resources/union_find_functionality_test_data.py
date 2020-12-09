

union_find_functionality_test_data: dict = {
    "test_0": {
        "params": {
            "n": 10,
            "queries": [
                ["union", 4, 3],
                ["union", 3, 8],
                ["union", 6, 5],
                ["union", 9, 4],
                ["union", 2, 1],
                ["connected", 8, 9],
                ["connected", 5, 4],
                ["union", 5, 0],
                ["union", 7, 2],
                ["union", 6, 1],
            ],
        },
        "expected": [
            None,
            None,
            None,
            None,
            None,
            True,
            False,
            None,
            None,
            None,
        ]
    }
}
