from grokking_algorithms.chapter2.selection_sort import (
    selection_sort_pythonic_way,
    selection_sort_classic,
)


def test_selection_sort_classic():
    arr = [1, 7, 9, 2, 6, 2, 5]
    assert selection_sort_classic(arr) == sorted(arr)


def test_selection_sort_pythonic_way():
    arr = [1, 7, 9, 2, 6, 2, 5]
    assert selection_sort_pythonic_way(arr) == sorted(arr)
