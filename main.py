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
    print("Palindrome")
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
                        elif twa.data() == "b":
                            twa.write("x")
                            break
                if twa.data() == "#":
                    twa.accept()
        except Exception as e:
            print(e)

def StringAEqualsToStringB():
    print("StringAEqualsToStringB")
    cases = [
        create_case("#abacaba#"),
        create_case("#abacaab#"),
        create_case("#babcbaa#"),
        create_case("#bacba#"),
        create_case("#aabcaa#")
    ]

    for each_case in cases:
        try:
            twa = TwoWayAccepter(each_case)
            print(f"CURRENT CASE {twa.chars()}")
            if twa.data() == "#":
                twa.right()

            while True:
                print(twa.chars())
                if twa.data() in ["x", "c"]:
                    twa.right()
                    continue
                elif twa.data() == "a":
                    twa.write("x")
                    twa.right()
                    while twa.data() in ["a", "b", "c"]:
                        twa.right()
                        if twa.data() == "c":
                            twa.right()
                            break

                    while True:
                        if twa.data() == "x":
                            twa.right()
                            continue
                        elif twa.data() == "a":
                            twa.write("x")
                            break
                        elif twa.data() in ["b", "#"]:
                            twa.reject()

                    while True:
                        if twa.data() in ["x", "c", "a", "b"]:
                            twa.left()
                        if twa.data() == "#":
                            twa.right()
                            break

                elif twa.data() == "b":
                    twa.write("x")
                    twa.right()
                    while twa.data() in ["a", "b", "c"]:
                        twa.right()
                        if twa.data() == "c":
                            twa.right()
                            break

                    while True:
                        if twa.data() == "x":
                            twa.right()
                            continue
                        elif twa.data() == "b":
                            twa.write("x")
                            break
                        elif twa.data() in ["a", "#"]:
                            twa.reject()

                    while True:
                        if twa.data() in ["x", "c", "a", "b"]:
                            twa.left()
                        if twa.data() == "#":
                            twa.right()
                            break
                elif twa.data() == "#":
                    twa.accept()

        except Exception as e:
            print(e)

def NumAEqualsNumB():
    print("NumAEqualsNumB")
    cases = [
        create_case("#aababb#"),
        create_case("#babbaa#"),
        create_case("#aabab#"),
        create_case("#babb#")
    ]

    for each_case in cases:
        try:
            twa = TwoWayAccepter(each_case)
            print(f"CURRENT CASE {twa.chars()}")

            if twa.data() == "#":
                twa.right()

        except Exception as e:
            print(e)

palindrome()
StringAEqualsToStringB()
