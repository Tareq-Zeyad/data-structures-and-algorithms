"""
Tests for Binary Tree
"""
from data_structures.data_structures.trees.trees import BinaryTree, Node, BinarySearchTree


def test_bfs():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node('A')
    b_node = Node('B')
    c_node = Node('C')
    d_node = Node('D')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected


def test_bfs_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected


def test_pre_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "4", "3"]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected


def test_post_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "3", "1"]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected


def test_in_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "1", "3"]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected


def test_binary_search_tree():
    # Arrange
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(4)
    tree.add(80)

    expected = [50, 4, 80]
    # Actual
    actual = tree.bfs()

    # Assert
    assert expected == actual


def test_binary_search_tree_contains():
    # Arrange
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(4)
    tree.add(80)
    expected = True
    # Actual
    actual = tree.contains(4)

    # Assert
    assert expected == actual


def test_binary_search_tree_doesnt_contain():
    # Arrange
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(4)
    expected = False
    # Actual
    actual = tree.contains(80)

    # Assert
    assert expected == actual


def test_instantiate_tree():
    # Arrange
    tree = BinarySearchTree()
    expected = True
    # Actual
    actual = False
    if tree:
        actual = True

    # Assert
    assert expected == actual


def test_instantiate_tree_single_root():
    # Arrange
    tree = BinarySearchTree()
    a_node = Node('1')
    tree.root = a_node
    expected = '1'
    # Actual
    actual = tree.root.data

    # Assert
    assert expected == actual


def test_instantiate_tree_root_left_right():
    # Arrange
    tree = BinarySearchTree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    a_node.left = b_node
    a_node.right = c_node

    tree.root = a_node
    expected = '2'
    # Actual
    actual = tree.root.left.data

    # Assert
    assert expected == actual
