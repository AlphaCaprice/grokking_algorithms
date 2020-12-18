def selection_sort_classic(array_list: list) -> list:
    """Mutating given list while sorting"""
    for i in range(len(array_list)):
        min_index = i
        for j in range(i, len(array_list)):
            if array_list[j] < array_list[min_index]:
                min_index = j
        array_list[i], array_list[min_index] = array_list[min_index], array_list[i]

    return array_list


def selection_sort_pythonic_way(array_list: list) -> list:
    """Mutating given list while sorting"""
    for i in range(len(array_list)):
        min_index = min(range(i, len(array_list)), key=array_list.__getitem__)
        array_list[i], array_list[min_index] = array_list[min_index], array_list[i]
    return array_list
