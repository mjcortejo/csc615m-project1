class Node():
    #Node definition for use in Doubly Linked List implementation
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = None
        self.next = None

#https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm
class DoublyLinkedList():
    #Will use Double linked list for this project to be able to traverse the elements using a left and right function
    def __init__(self):
        self.head = None

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

class TwoWayAccepter():
    #Defining a Two Way Accepter Machine that will use the Double Linked List as its input
    def __init__(self, case):# Accepts Double Linked List object
        self.original = case.head
        self.current = case.head

    def left(self):
        self.current = self.current.prev

    def right(self):
        self.current = self.current.next

    def data(self):
        return self.current.data

    def write(self, char):
        self.current.data = char
        # print(self.chars())

    def chars(self):
        node = self.original
        chars = ""
        while node is not None:
            chars = chars + node.data
            node = node.next
        return chars

    def accept(self):
        """
        Raise exception if accepted to terminate the entire function body for this case
        """
        raise Exception("ACCEPTED")

    def reject(self):
        """
        Raise exception if rejected to terminate the entire function body for this case
        """
        raise Exception("REJECTED")

def create_case(string):
    """
    Creates a case of DoubleLinkedList objects from a string input
    """
    input_string = DoublyLinkedList()
    for each_char in string:
        input_string.append(each_char)
    return input_string

def simulator(cases, program):
    """
    Defines the simulator that accepts cases and a program object
    """
    for each_case in cases:
        try:
            twa = TwoWayAccepter(each_case)
            current_state = 1

            if twa.data() == "#":
                twa.right()

            transition_set = program[str(current_state)]
            instruction = transition_set[twa.data()]

            while True:
                if type(instruction) == int:
                    instruction = transition_set[twa.data()]
                    transition_set = program[str(instruction)]
                    if transition_set['dir'] == 'left':
                        twa.left()
                    elif transition_set['dir'] == 'right':
                        twa.right()
                elif instruction == 'accept':
                    twa.accept()
                elif instruction == 'reject':
                    twa.reject()

        except Exception as e:
            print(e)
            pass
