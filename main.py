from structure import DoublyLinkedList

class TwoWayAccepter():
    def __init__(self, case):# Accepts Double Linked List object
        self.current = case.head

    def left(self):
        self.current = self.current.prev

    def right(self):
        self.current = self.current.next

    def data(self):
        return self.current.data

def create_case(string):
    input_string = DoublyLinkedList()
    for each_char in string:
        input_string.append(each_char)
    return input_string

def palindrome():
    cases = []
    cases.append(create_case("#ababcabab#"))

def NumAEqualsNumB():
    cases = []
    cases.append(create_case("#abacaba#"))

NumAEqualsNumB()
