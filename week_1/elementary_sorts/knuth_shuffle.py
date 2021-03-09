from random import randint


def shuffle(arr: list):
    n: int = len(arr)
    for i in range(0, n):
        r: int = randint(0, i)
        exchange(arr, i, r)


def exchange(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]
