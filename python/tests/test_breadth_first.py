import pytest
from code_challenges.tree_breadth_first.tree_breadth_first import breadth_first, BinaryTree, Node


def test_expected_outcome(binary_tree):
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = breadth_first(binary_tree)
    assert actual == expected


def test_expected_failure(empty_binary_tree):
    expected = None
    actual = breadth_first(empty_binary_tree)
    assert actual == expected


@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    a_node = Node(2)
    b_node = Node(7)
    c_node = Node(5)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = Node(2)
    d_node = Node(6)
    d_node.left = Node(5)
    d_node.right = Node(11)
    b_node.right = d_node
    e_node = Node(9)
    c_node.right = e_node
    e_node.left = Node(4)
    tree.root = a_node
    return tree


@pytest.fixture
def empty_binary_tree():
    tree = BinaryTree()
    return tree
