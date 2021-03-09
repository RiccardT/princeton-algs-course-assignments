

def shell_sort(arr: list):
    n: int = len(arr)
    h: int = 1
    while h < n//3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, n):
            j: int = i
            while j >= h and is_less(arr[j], arr[j - h]):
                exchange(arr, j, j - h)
                j -= h
        h = h//3


def is_less(v: any, w: any) -> bool:
    return v < w


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [1, 9, 0, 1, 4, 5, 8, 10, 11, 0]
    print(arr)
    shell_sort(arr)
    print(arr)
