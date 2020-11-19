class Node():
    def __init__(self, data, prev=None, next=None)
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self, input_string):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


            