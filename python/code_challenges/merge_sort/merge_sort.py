import math


def merge_sort(_list: list):
    """Merge Using Sort method
    Args:
        _list (list): List to be merged.
    Returns:
        list (list): Sorted List
    """

    n = len(_list)
    if n > 1:
        mid = math.floor(n/2)
        left = _list[:mid]
        right = _list[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, _list)

    return _list


def merge(left, right, _list):
    """Merge right and left in one list
    Args:
        left ([list]): left of list
        right ([list]): right of the list
        _list ([type]): original list
    Returns:
        None
    """
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            _list[k] = left[i]
            i += 1
        else:
            _list[k] = right[j]
            j += 1
        k += 1

    while j < len(right):
        _list[k] = right[j]
        j += 1
        k += 1
    while i < len(left):
        _list[k] = left[i]
        i += 1
        k += 1
