from grokking_algorithms.chapter3.recursion import count_items, example_tree


def test_count_items():
    assert count_items(example_tree, "RED") == 6
