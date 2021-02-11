from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests


def brute_force(bitonic_array: list, value: int) -> bool:  # ~3Log(n)
    inflection_point: int = get_bitonic_inflection_index_with_bs(bitonic_array)
    left_side_search_value: int = find_value_reg_bs(bitonic_array[:inflection_point], value)
    if left_side_search_value != -1:
        return True
    right_side_search_value: int = find_value_reverse_bs(bitonic_array[inflection_point:], value)
    if right_side_search_value != -1:
        return True
    return False


def optimal(bitonic_array: list, value: int) -> bool:
    return bitonic_search(bitonic_array, value)


def bitonic_search(bitonic_arr: list, value: int) -> bool:
    if len(bitonic_arr) == 0:  # Base Case 0
        return False
    middle_index: int = len(bitonic_arr) // 2
    left_index, right_index = middle_index - 1, middle_index + 1
    middle_value: int = bitonic_arr[middle_index]
    if middle_value == value:  # Base Case 1
        return True
    elif len(bitonic_arr) == 1:  # Base Case 2
        return False
    if left_index < 0 or right_index >= len(bitonic_arr):
        return False
    left_value: int = bitonic_arr[left_index]
    right_value: int = bitonic_arr[right_index]
    if (left_value > middle_value > right_value) and (value > middle_value):
        return bitonic_search(bitonic_arr[:middle_index], value)
    elif (left_value < middle_value < right_value) and (value > middle_value):
        return bitonic_search(bitonic_arr[middle_index:], value)
    elif value < middle_value:
        left_search_value: int = find_value_reg_bs(bitonic_arr[:middle_index], value)
        if left_search_value != -1:
            return True
        right_search_value: int = find_value_reverse_bs(bitonic_arr[middle_index:], value)
        if right_search_value != -1:
            return True
        return False


def get_bitonic_inflection_index_with_bs(arr: list) -> int:  # O(log(n)
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


def find_value_reg_bs(arr: list, value: int) -> int:  # O(log(n)
    begin: int = 0
    end: int = len(arr) - 1
    mid: int = 0
    while begin <= end:
        mid = (begin + end) // 2
        if value > arr[mid]:
            begin = mid + 1
        elif value < arr[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def find_value_reverse_bs(arr: list, value: int) -> int:  # O(log(n)
    begin: int = 0
    end: int = len(arr) - 1
    mid: int = 0
    while begin <= end:
        mid = (begin + end) // 2
        if value < arr[mid]:
            begin = mid + 1
        elif value > arr[mid]:
            end = mid - 1
        else:
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
        },
        "test_2": {
            "params": {
                "bitonic_array": [1, 2, 3, 1],
                "value": 2
            },
            "expected": True
        },
        "test_3": {
            "params": {
                "bitonic_array": [23, 24, 69, 100, 99, 79, 78, 67, 36, 26, 19],
                "value": 67
            },
            "expected": True
        }
    }
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
