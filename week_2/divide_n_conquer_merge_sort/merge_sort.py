from week_2.merge import merge


def sort(arr: list):
    n: int = len(arr)
    aux: list = [0] * n
    recursive_sort(a, aux, 0, n - 1)


def recursive_sort(a: list, aux: list, lo: int, hi: int):
    if hi <= lo:
        return
    mid: int = lo + (hi - lo)//2
    recursive_sort(a, aux, lo, mid)
    recursive_sort(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)


if __name__ == '__main__':
    a = [1, 0, 3, 6, 2, 3, 9, 8]
    print(a)
    sort(a)
    print(a)
