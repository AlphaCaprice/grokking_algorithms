"""
There wasn't a good recursion example in the book ,
so I took this task as a great showing of recursion power:

Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

"""
from typing import Union

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def count_items(node: dict, item: Union[list, set, tuple]):
    if node == item:
        return 1
    if isinstance(node, (list, set, tuple)):
        return sum(count_items(nested_node, item) for nested_node in node)
    if isinstance(node, dict):
        return sum(count_items(nested_node, item) for nested_node in node.values())
    return 0
