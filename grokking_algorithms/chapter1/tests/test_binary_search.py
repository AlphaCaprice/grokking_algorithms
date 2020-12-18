import pytest
from grokking_algorithms.chapter1.binary_search import (
    binary_search,
    binary_search_bisect,
)


def parameters():
    return (
        ["array_list", "item", "result"],
        [
            ([1, 3, 5, 6, 8, 9], 5, 2),
            ([1, 3, 5, 6, 8, 9], 9, 5),
            ([1, 3, 5, 6, 8, 9], 1, 0),
            ([1, 3, 5, 6, 8, 9], 4, -1),
            ([1, 3, 5, 6, 8, 9], 10, -1),
            ([1, 3, 5, 6, 8, 9], 0, -1),
            ([1, 3, 5, 8, 9], 5, 2),
            ([1, 3, 5, 8, 9], 1, 0),
            ([1, 3, 5, 8, 9], 9, 4),
            ([1, 3, 5, 8, 9], 4, -1),
            ([1, 3, 5, 8, 9], 10, -1),
            ([1, 3, 5, 8, 9], 0, -1),
        ],
    )


@pytest.mark.parametrize(*parameters())
def test_binary_search(array_list, item, result):
    assert binary_search(array_list, item) == result


@pytest.mark.parametrize(*parameters())
def test_binary_search_bisect(array_list, item, result):
    assert binary_search_bisect(array_list, item) == result
