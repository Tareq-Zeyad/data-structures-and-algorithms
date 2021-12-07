def quick_sort(arr, left, right):
    """A method that sorts a list following the quicksort algorithm
    Args:
        arr ([list]): list to be sorted.
        left ([int]): index of first element
        right ([int]): indext of last element
    Returns:
        [list]: Sorted List
    """
    if left < right:
        postion = partition(arr, left, right)
        quick_sort(arr, left, postion - 1)
        quick_sort(arr, postion + 1, right)

    return arr


def partition(arr, left, right):
    """split provided array into parts
    Args:
        arr ([list]): list to be partitioned
        left ([int]): left index
        right ([int]): right index
    Returns:
        [int]: lowest index + 1
    """
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)
    swap(arr, right, low + 1)
    return low + 1


def swap(arr, i, low):
    """Swap 2 values in 1 list
    Args:
        arr ([list]): list to swap items in
        i ([int]): first index
        low ([int]): second index
    """
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
