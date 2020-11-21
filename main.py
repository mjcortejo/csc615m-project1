from structure import DoublyLinkedList

class TwoWayAccepter():
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
        print(self.chars())

    def chars(self):
        node = self.original
        chars = ""
        while node is not None:
            chars = chars + node.data
            node = node.next
        return chars

    def accept(self):
        raise Exception("ACCEPTED")

    def reject(self):
        raise Exception("REJECTED")

def create_case(string):
    input_string = DoublyLinkedList()
    for each_char in string:
        input_string.append(each_char)
    return input_string

def palindrome():
    cases = [
        create_case("#abacaba#"),
        create_case("#abacabb#"),
        create_case("#abacbab#")
    ]

    for each_case in cases:
        try:
            twa = TwoWayAccepter(each_case)
            print(f"CURRENT CASE {twa.chars()}")
            if twa.data() == "#":
                twa.right()

            while twa.data() in ["a", "b"]:
                twa.right()
                if twa.data() == "c":
                    break

            while twa.data() in ["c", "x"]:
                twa.right()
                if twa.data() == "a":
                    twa.write("x")
                    while twa.data() in ["c", "x"]:
                        twa.left()
                        if twa.data() == "b":
                            twa.reject()
                        elif twa.data() == "a":
                            twa.write("x")
                            break
                if twa.data() == "b":
                    twa.write("x")
                    while twa.data() in ["c", "x"]:
                        twa.left()
                        if twa.data() == "a":
                            twa.reject()
                            continue
                        elif twa.data() == "b":
                            twa.write("x")
                            break
                if twa.data() == "#":
                    twa.accept()
        except Exception as e:
            print(e)

# def StringAEqualsToStringB():
#     cases = [
#         create_case("#aabcaab#"),
#         create_case("#abacaab#"),
#         create_case("#babcbaa#"),
#         create_case("#aabcaa#")
#     ]
#
#     for each_case in cases:
#         twa = TwoWayAccepter(each_case)
#         print(f"CURRENT CASE {twa.chars()}")
#
#         if twa.data() == "#":
#             twa.right()


palindrome()
# StringAEqualsToStringB()
