from random import shuffle

from week_2.quick_sort.partition import partition


def find_kth_smallest_item(a: list, k: int):
    shuffle(a)
    lo: int = 0
    hi: int = len(a) - 1
    while hi > lo:
        j: int = partition(a, lo, hi)
        if k_is_on_right_partition(j, k):
            lo = j + 1
        elif k_is_on_left_partition(j, k):
            hi = j - 1
        else:
            return a[k]
    return a[k]


def k_is_on_right_partition(j: int, k: int) -> bool:
    return j < k


def k_is_on_left_partition(j: int, k: int) -> bool:
    return j > k


if __name__ == '__main__':
    a = [1, 3, 9, 0, 4, 7, 2, 5]
    print(a)
    print(find_kth_smallest_item(a, 4))
    print(sorted(a))
