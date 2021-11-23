from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree, BinaryTree, Node
import pytest


def test_expected_outcome(binary_tree):
    # Arrange
    expected = ["Buzz", "Fizz", "Buzz", "7", "1", "FizzBuzz"]
    # Actual
    new_tree = fizz_buzz_tree(binary_tree)
    actual = new_tree.bfs()
    # Outcome
    assert actual == expected


def test_empty_binary_tree(empty_binary_tree):
    # Arrange
    expected = None
    # Actual
    new_tree = fizz_buzz_tree(empty_binary_tree)
    actual = new_tree.bfs()
    # Outcome
    assert actual == expected


@pytest.fixture
def binary_tree():
    tree = BinaryTree()
    a_node = Node(5)
    b_node = Node(3)
    c_node = Node(5)
    b_node.left = Node(7)
    b_node.right = Node(1)
    c_node.right = Node(15)
    a_node.left = b_node
    a_node.right = c_node
    tree.root = a_node
    return tree


@pytest.fixture
def empty_binary_tree():
    tree = BinaryTree()
    return tree
