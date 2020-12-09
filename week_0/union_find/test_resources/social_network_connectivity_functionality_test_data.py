from week_0.union_find.interview_questions.social_network_connectivity.Connection import Connection


social_network_connectivity_functionality_test_data: dict = {
    "test_0": {
        "params": {
            "connections": [
                Connection(3, 1, 0),
                Connection(2, 0, 1),
                Connection(1, 3, 2),
            ],
            "friends": 4
        },
        "expected": 2
    }
}
