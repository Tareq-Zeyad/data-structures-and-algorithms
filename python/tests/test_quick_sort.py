from code_challenges.quick_sort.quick_sort import quick_sort


def test_quick_sort_one():
    # Arange
    list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 41]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Assert
    actual == expected


def test_quick_sort_two():
    # Arrange
    list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected


def test_quick_sort_three():
    # Arrange
    list = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected


def test_quick_sort_four():
    # Arrange
    list = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected


def test_quick_sort_five():
    # Arrange
    list = [-2, -5]
    expected = [-5, -2]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected


def test_quick_sort_one_item_list():
    # Arrange
    list = [1]
    expected = [1]
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected


def test_quick_sort_empty_list():
    # Arrange
    list = []
    expected = []
    # Actual
    actual = quick_sort(list, 0, len(list)-1)
    # Expected
    assert actual == expected
