from bisect import bisect

from typing import Any


def binary_search(array_list: list, item: Any) -> int:
    low = 0
    high = len(array_list) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = array_list[middle]
        if guess == item:
            return middle
        elif guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return -1


def binary_search_bisect(array_list: list, item: Any) -> int:
    pos = bisect(array_list, item) - 1
    return pos if array_list[pos] == item else -1
