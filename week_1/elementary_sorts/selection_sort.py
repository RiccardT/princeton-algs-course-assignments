

def selection_sort(arr: list) -> None:
    n: int = len(arr)
    for i in range(n):
        min_index: int = i
        for j in range(i + 1, n):
            if is_less(arr[j], arr[min_index]):
                min_index = j
        exchange(arr, i, min_index)


def is_less(v: any, w: any) -> bool:
    return v < w


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [1, 2, 4, 2, 0, 5, 6]
    print(arr)
    selection_sort(arr)
    print(arr)
