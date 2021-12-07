from code_challenges.merge_sort.merge_sort import merge_sort


def test_merge_sort_one():
    # Arrange
    expected = [4, 8, 15, 16, 23, 42]
    # Actual
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    # Expected
    assert actual == expected


def test_merge_sort_two():
    # Arrange
    expected = [-2, 5, 8, 12, 18, 20]
    # Actual
    actual = merge_sort([20, 18, 12, 8, 5, -2])
    # Expected
    assert actual == expected


def test_merge_sort_three():
    # Arrange
    expected = [5, 5, 5, 7, 7, 12]
    # Actual
    actual = merge_sort([5, 12, 7, 5, 5, 7])
    # Expected
    assert actual == expected


def test_merge_sort_four():
    # Arrange
    expected = [2, 3, 5, 7, 11, 13]
    # Actual
    actual = merge_sort([2, 3, 5, 7, 13, 11])
    # Expected
    assert actual == expected


def test_merge_sort_edge_case_one():
    # Arrange
    expected = [2, 5]
    # Actual
    actual = merge_sort([5, 2])
    # Expected
    assert actual == expected


def test_merge_sort_edge_case_two():
    # Arrange
    expected = [2]
    # Actual
    actual = merge_sort([2])
    # Expected
    assert actual == expected


def test_merge_sort_empty():
    # Arrange
    expected = []
    # Actual
    actual = merge_sort([])
    # Expected
    assert actual == expected
