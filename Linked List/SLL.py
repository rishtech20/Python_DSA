class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''Append value x at the end of the list'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += f"{curr.data}->"
            curr = curr.next

        if to_print:
            return f"[{to_print[:-2]}]"

        return "[]"

    def add_to_start(self, x):
        '''Add x to the start of the list' making it the head'''
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
            self.tail = x
        else:
            old_val = self.head
            self.head = x
            self.head.next = old_val

    def search_val(self, x):
        '''Return the indices where x was found'''
        pass

    def remove_val_by_index(self, x):
        '''remove and return the value at the index x provided as parameter'''
        pass

    def length(self):
        '''return the length of the list represented by the number of nodes'''
        pass

    def reverse_list_recur(self, current, previous):
        '''Reverse the sequence of the node pointers in the linked list'''
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

my_list = SinglyLinkedList()

print(my_list)

my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
my_list.append_val(node6)

print(my_list)

node7 = Node(10)

my_list.add_to_start(node7)

print(my_list)
