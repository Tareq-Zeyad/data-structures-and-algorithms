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


def append(self, value):
    """
    Add a value at the end of a linked list, if no value exists, it will be the head of the list.
    """
    current = self.head

    if(current != None):
        while(True):
            if current.next != None:
                current = current._next
            else:
                current.next = Node(value)
                break
    else:
        self.head = Node(value)


def insert_before(self, before_value, value):
    """
    Insert a given value before a specificed itme in the linked list.
    """
    current = self.head

    if(current != None):
        while(True):
            if current._next == None:
                if current.data == before_value:
                    self.head = Node(value, current)
                    break
                else:
                    break
            elif current._next.data == before_value:
                current._next = Node(value, current._next)
                break
            else:
                current = current._next
    else:
        self.head = Node(value)


def insert_after(self, after_value, value):
    """
    Insert a given value after a specificed item in the linked list.
    """
    current = self.head

    if(current != None):
        while(True):
            if current._next == None:
                if current.data == after_value:
                    current._next = Node(value, current._next)
                    break
                else:
                    break
            elif current.data == after_value:
                current._next = Node(value, current._next)
                break
            else:
                current = current._next



def kthFromEnd(self, input):
    current = self.head

    if input == 1:
        return current.data
    elif(current != None and current._next != None and input > 0):
        count = 1
        second_pointer = [None]

        while(True):
            if count == input:
                second_pointer[0] = current
            elif count - input == input:
                second_pointer[0] = second_pointer[0]._next

            if current._next == None:
                if(count < input):
                    return None
                else:
                    return second_pointer[0].data
            else:
                current = current._next
                count += 1

    elif (current != None and current._next != None and input == 0):
        while(True):
            if current._next == None:
                return current.data
            else:
                current = current._next
    else:
        return None



if __name__ == '__main__':

    ll = LinkedList()

    ll.append(7)
    ll.append(1)
    ll.append(2)
