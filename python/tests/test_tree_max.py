from data_structures.data_structures.trees.trees import BinaryTree, Node


def test_expected_outcome():
    # Arrange
    tree = BinaryTree()
    a_node = Node(5)
    b_node = Node(10)
    c_node = Node(25)
    d_node = Node(3)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node
    expected = 25
    # Actual
    actual = tree.find_highest()
    # Assert
    assert actual == expected


def test_expected_failure():
    # Arrange
    tree = BinaryTree()
    expected = False
    # Actual
    actual = tree.find_highest()
    # Assert
    assert actual == expected


def test_edge_case_wrong_tree():
    # Arrange
    tree = BinaryTree()
    a_node = Node("2")
    b_node = Node("6")
    c_node = Node("61")
    a_node.left = b_node
    a_node.right = c_node
    tree.root = a_node
    expected = 61
    # Actual
    actual = tree.find_highest()
    # Assert

    assert actual == expected
