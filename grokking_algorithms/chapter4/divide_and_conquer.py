import random


def recursion_sum(array_list: list) -> int:
    if not array_list:
        return 0
    return array_list[0] + recursion_sum(array_list[1:])


def recursion_max(array_list: list) -> int:
    if len(array_list) == 1:
        return array_list[0]
    max_element = recursion_max(array_list[1:])
    return array_list[0] if array_list[0] > max_element else max_element


def quick_sort(array_list: list) -> list:
    """Use a lot of additional memory,
    but easy to read and understand the concept."""
    if len(array_list) <= 1:
        return array_list
    pivot = random.choice(array_list)

    less = [element for element in array_list if element < pivot]
    equal = [pivot] * array_list.count(pivot)
    greater = [element for element in array_list if element > pivot]

    return list(quick_sort(less) + equal + quick_sort(greater))
