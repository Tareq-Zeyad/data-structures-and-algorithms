from code_challenges.insertion_sort.insertion_sort import insertion_sort


def test_insertion_sort_one():
    # Arrange
    list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected


def test_insertion_sort_two():
    # Arrange
    list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected


def test_insertion_sort_three():
    # Arrange
    list = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected


def test_insertion_sort_four():
    # Arrange
    list = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected


def test_insertion_sort_empty_list():
    # Arrange
    list = []
    expected = []
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected


def test_insertion_sort_failure():
    # Arrange
    list = 5
    expected = None
    # Actual
    actual = insertion_sort(list)
    # Assert
    assert actual == expected
