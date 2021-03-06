"""
This Module defines a Node and a Binary Tree
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class BinaryTree:

    def __init__(self):
        self.root = None

    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        """
        # Queue breadth <-- new Queue()
        breadth = Queue()
        # breadth.enqueue(root)
        breadth.enqueue(self.root)

        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.data]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        sub method : walk () to make the recursion staff
        """
        list_of_items = []

        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def in_order(self):
        """
        function to in order the list using Trees
        """
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.data)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def post_order(self):
        """
        A binary tree method which returns a list of items in post order
        input: None
        output: tree items
        """
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

            list_of_items.append(node.data)

        walk(self.root)
        return list_of_items


class BinarySearchTree(BinaryTree):
    """
    Binary Tree Class
    A class that extends BiaryTree class with 2 new methods:
    Method: Add
        Args:
        value
    Returns:
        None
    Method: Contains
        Args:
            Value
        Returns:
            True or False
    """

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            if self.root.data < data:
                if not self.root.right:
                    self.root.right = Node(data)
                else:
                    self.add(data)
            else:
                if not self.root.left:
                    self.root.left = Node(data)
                else:
                    self.add(data)

    def contains(self, value):
        items = self.bfs()

        for item in items:
            if item == value:
                return True
        return False


def find_max(self):
    """
    A binary tree method which returns the maximun value in the tree
    input: Binary Tree
    output: highest value
    """
    max_found = 0

    def walk(node):
        nonlocal max_found
        if node:
            if int(node.data) > max_found:
                max_found = int(node.data)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        else:
            max_found = False
    walk(self.root)
    return max_found
