from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force(numbers: list, value: int) -> tuple:  # ~N^3
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == value:
                    return i, j, k
    return -1, -1, -1


def optimal(numbers: list, value: int) -> tuple:  # O(n^2) -> ~ n^2
    hashed_numbers: dict = {}
    for number in numbers:
        hashed_numbers[number] = number
    for i in numbers:
        for j in numbers:
            difference: int = value - (i + j)
            if difference in hashed_numbers:
                return i, j, hashed_numbers[difference]
    return -1, -1, -1


if __name__ == '__main__':
    functionality_test_data: dict = {
        "test_0": {
            "params": {
                "numbers": [1, 2, 3, 4, 5, 6, 7, 8],
                "value": 11
            },
            "expected": (1, 2, 8)
        }
    }
    dynamically_generate_tests(functionality_test_data, optimal)
    run_dynamic_tests()
