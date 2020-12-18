import pytest

from grokking_algorithms.chapter4.divide_and_conquer import (
    recursion_sum,
    recursion_max,
    quick_sort,
)


@pytest.mark.parametrize("arr", [[5, 3, 2, 10, 4, 6], []])
def test_recursion_sum(arr):
    assert recursion_sum(arr) == sum(arr)


def test_recursion_max():
    arr = [1, 6, 8, 2, 4]
    assert recursion_max(arr) == max(arr)


def test_quick_sort():
    arr = [1, 6, 8, 2, 6, 8, 10, 2, 5, 7, 22]
    assert quick_sort(arr) == sorted(arr)
