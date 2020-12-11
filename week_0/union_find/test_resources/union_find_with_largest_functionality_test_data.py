

union_find_with_find_largest_functionality_test_data: dict = {
    "test_0": {
        "params": {
            "n": 10,
            "queries": [
                ["union", 4, 3],
                ["union", 3, 8],
                ["union", 6, 5],
                ["union", 9, 4],
                ["union", 2, 1],
                ["union", 5, 0],
                ["union", 7, 2],
                ["union", 6, 1],
                ["union", 7, 3],
                ["find", 6]
            ],
        },
        "expected": [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            9
        ]
    }
}
