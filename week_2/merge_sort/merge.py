

def merge(a: list, aux: list, lo: int, mid: int, hi: int):
    assert(is_sorted(a, lo, mid))
    assert(is_sorted(a, mid + 1, hi))
    for k in range(lo, hi + 1):
        aux[k] = a[k]
    i: int = lo
    j: int = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif is_less(aux[j], aux[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1
    assert(is_sorted(a, lo, hi))


def is_sorted(a: list, lo: int, hi: int) -> bool:
    for i in range(lo, hi):
        if not a[i] <= a[i + 1]:
            return False
    return True


def is_less(v: any, w: any) -> bool:
    return v < w


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    a: list = [1, 2, 3, 4, 5]
    b: list = [3, 4, 5, 6, 7]
    c = a + b
    print(c)
    n = len(c)
    lo = 0
    mid = n//2 - 1
    hi = n - 1
    aux = [0]*n
    merge(c, aux, lo, mid, hi)
    print(c)
