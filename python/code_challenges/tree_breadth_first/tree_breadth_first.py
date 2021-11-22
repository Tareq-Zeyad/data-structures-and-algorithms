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


def breadth_first(tree: BinaryTree):
    if not tree.root:
        return None
    breadth = Queue()
    breadth.enqueue(tree.root)

    list_of_items = []

    while breadth.peek():
        front = breadth.dequeue()
        list_of_items += [front.data]

        if front.left:
            breadth.enqueue(front.left)

        if front.right:
            breadth.enqueue(front.right)

    return list_of_items
