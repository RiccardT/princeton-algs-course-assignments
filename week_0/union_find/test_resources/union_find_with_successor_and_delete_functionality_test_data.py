

union_find_with_successor_and_delete_functionality_test_data: dict = {
    "test_0": {
        "params": {
            "n": 10,
            "queries": [
                ["remove", 5],
                ["successor", 4],
                ["remove", 6],
                ["successor", 4]
            ],
        },
        "expected": [
            None,
            6,
            None,
            7
        ]
    }
}