from random import shuffle


def partition(a: list, lo: int, hi: int):
    partition_index: int = lo
    i: int = partition_index + 1
    j: int = hi
    while True:
        i = move_i_right_for_all_elements_less_than_partition_index(a, i, partition_index, hi)
        j = move_j_left_for_all_elements_greater_than_partition_index(a, j, partition_index)
        if i >= j:
            break
        exchange(a, i, j)
    exchange(a, partition_index, j)
    partition_index = j
    return partition_index


def move_i_right_for_all_elements_less_than_partition_index(a: list, i: int, partition_index: int, hi: int):
    while is_less(a[i], a[partition_index]):
        i += 1
        if i == hi:
            break
    return i


def move_j_left_for_all_elements_greater_than_partition_index(a: list, j: int, pivot: int):
    while is_greater(a[j], a[pivot]):
        j -= 1
        if j == pivot:
            break
    return j


def is_less(v: any, w: any) -> bool:
    return v < w


def is_greater(v: any, w: any) -> bool:
    return v > w


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    a = [1, 0, 4, 5, 6, 3, 0, 10, 9, 8, 2]
    shuffle(a)
    print(a)
    print(partition(a, 0, len(a) - 1))
    print(a)
