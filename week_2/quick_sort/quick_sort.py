from random import shuffle

from week_2.quick_sort.partition import partition


def quick_sort(a: list):
    shuffle(a)
    recursive_sort(a, 0, len(a) - 1)


def recursive_sort(a: list, lo: int, hi: int):
    if hi <= lo:
        return
    j: int = partition(a, lo, hi)
    recursive_sort(a, lo, j - 1)
    recursive_sort(a, j + 1, hi)


if __name__ == '__main__':
    a = [2, 0, 4, 3, 6, 8, 4, 6, 0, 1]
    print(a)
    quick_sort(a)
    print(a)

