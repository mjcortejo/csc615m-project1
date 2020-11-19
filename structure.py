class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = None
        self.next = None

#https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm
class DoublyLinkedList():
    def __init__(self):
        self.head = None

    # def push(self, data):
    #     node = Node(data)
    #     node.next = self.head
    #     if self.head is not None:
    #         self.head.prev = node
    #     self.head = node
    #     print(f"Current head: {self.head.data}")

    def append(self, data):
        node = Node(data)
        node.next = None
        if self.head is None:
            node.prev = None
            self.head = node
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = node
        node.prev = last
        return

    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next