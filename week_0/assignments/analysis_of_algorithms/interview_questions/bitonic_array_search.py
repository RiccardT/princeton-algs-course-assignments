from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force(bitonic_array: list, value: int) -> bool:
    print(get_bitonic_inflection_index_with_bs(bitonic_array))
    return False


def get_bitonic_inflection_index_with_bs(arr: list) -> int:  # O(log(n), working
    begin: int = 0
    end: int = len(arr) - 1
    mid: int = 0
    while begin <= end:
        mid = (begin + end) // 2
        if (arr[mid - 1] < arr[mid]) and (arr[mid] < arr[mid + 1]):  # Inside increasing sequence
            begin = mid + 1
        elif (arr[mid - 1] > arr[mid]) and (arr[mid] > arr[mid + 1]):  # Inside decreasing sequence
            end = mid - 1
        elif (arr[mid - 1] < arr[mid]) and (arr[mid] > arr[mid + 1]):  # Found inflection
            return mid
    return -1


if __name__ == '__main__':
    functionality_test_data: dict = {
        "test_0": {
            "params": {
                "bitonic_array": [-3, 9, 18, 20, 17, 5, 1],
                "value": 20
            },
            "expected": True
        },
        "test_1": {
            "params": {
                "bitonic_array": [5, 6, 7, 8, 9, 10, 3, 2, 1],
                "value": 30
            },
            "expected": False
        }
    }
    dynamically_generate_tests(functionality_test_data, brute_force, timed=True)
    run_dynamic_tests()