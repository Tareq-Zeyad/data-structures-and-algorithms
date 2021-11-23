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
        A binary tree method that will return a list of items which it contains
        input: None
        output: tree items
        """
        if not self.root:
            return None
        breadth = Queue()
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


def fizz_buzz_tree(tree: BinaryTree):
    fizz_buzz_tree = BinaryTree()
    if not tree.root:
        return fizz_buzz_tree
    fizz_buzz_tree.root = Node(tree.root.data)
    queue = Queue()
    queue.enqueue(tree.root)
    second_queue = Queue()
    second_queue.enqueue(fizz_buzz_tree.root)

    while queue.peek():
        front = queue.dequeue()
        _front = None
        if second_queue.peek():
            _front = second_queue.dequeue()

        if _front.data % 3 == 0 and _front.data % 5 == 0:
            _front.data = "FizzBuzz"
        elif _front.data % 3 == 0:
            _front.data = "Fizz"
        elif _front.data % 5 == 0:
            _front.data = "Buzz"
        else:
            _front.data = str(_front.data)

        if front.left:
            queue.enqueue(front.left)
            _front.left = Node(front.left.data)
            second_queue.enqueue(_front.left)

        if front.right:
            queue.enqueue(front.right)
            _front.right = Node(front.right.data)
            second_queue.enqueue(_front.right)

    return fizz_buzz_tree
