from week_2.merge import merge


def sort(a: list):
    n: int = len(a)
    aux: list = [None]*n
    size: int = 1
    while size < n:
        lo = 0
        while lo < n - size:
            merge(a, aux, lo, lo + size - 1, min(lo + 2*size - 1, n - 1))
            lo += 2*size
        size *= 2


if __name__ == '__main__':
    a = [1, 0, 5, 2, 5, 10, 11, 0, 3]
    print(a)
    sort(a)
    print(a)
