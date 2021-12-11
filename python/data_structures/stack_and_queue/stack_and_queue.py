
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    """
    A class to implement the stack data structure.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise Exception("not allowed to pop an empty stack")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        return temp.value

    def peek(self):
        if not self.top:
            raise Exception("empty stack, no top value found")
        else:
            return self.top.value

    def is_empty(self):
        return self.top == None


class Queue:
    """
        A class to implement the queue data structure.

    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            raise Exception("the queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None

        return temp.value

    def peek(self):
        if not self.front:
            raise Exception("no top value, queue is empty")
        else:
            return self.front.value

    def is_empty(self):
        return self.front == None
