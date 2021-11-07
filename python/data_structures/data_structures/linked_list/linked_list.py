class Node:
    """
    Node class has the properties for the value in the Node, & a pointer to the next node.
    """
    counter = 0

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Class for Linked List for creating Nodes
    """

    def __init__(self):
        self.head = None

    def insert(self, addValue):
        node = Node(addValue)
        if self.head is None:
            self.head - node

        else:
            current = self.head
            while current.next != None:
                current = current.next

                LinkedList.counter += 1
                current.next = node
                return "Value is added"


@classmethod
def countering(cls):
    return cls.counter


def __str__(self):
    output = ""
    if self.head is None:
        output += None
    else:
        current = self.head
        while(current):

            output += ("{"+str(current.value)+"}"+" -> ")
            current = current.next
        output += "None"
        return output


def includes(self, valueSearched):
    """
    method to search for a specifc value
    """
    current = self.head
    if self.head != None:
        while current.next != None:
            if current.value == valueSearched:
                print("true")
                return True

            current = current.next
        print("false")
        return False
    else:
        print("Empty")
        return ("Empty")


if __name__ == '__main__':

    ll = LinkedList()

    ll.append(7)
    ll.append(1)
    ll.append(2)
