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
        # print(self.chars())

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

def NumAEvenAndNumBOdd():

    program = {
        '1': {'a': 1, '#': 'reject', 'b': 2, 'dir': 'right'},
        '2': {'a': 2, 'b': 1, '#': 3, 'dir': 'right'},
        '3': {'a': 3, 'b': 3, '#': 4, 'dir': 'left'},
        '4': {'a': 5, 'b': 4, '#': 'accept', 'dir': 'right'},
        '5': {'a': 4, 'b': 5, '#': 'reject', 'dir': 'right'}
    }
    print("NumAEvenNumBOdd")
    cases = [
        create_case("#aabbb#"),
        create_case("#aabb#"),
        create_case("#baa#"),
        create_case("#aaab#"),
    ]

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

def NumAEvenOrNumBOdd():
    program = {
        '1': {'a': 1, 'b': 2, '#': 3, 'dir': 'right'},
        '2': {'a': 2, 'b': 1, '#': 'accept', 'dir': 'right'},
        '3': {'a': 3, 'b': 3, '#': 4, 'dir': 'left'},
        '4': {'a': 5, 'b': 4, '#': 'accept', 'dir':'right'},
        '5': {'a': 4, 'b': 5, '#': 'reject', 'dir': 'right'}
    }
    print("NumAEvenOrNumBOdd")
    cases = [
        create_case("#aabbb#"), #accept
        create_case("#abb#"), #reject
        create_case("#baa#"), #accept
        create_case("#aaabb#"), #reject
    ]

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
# NumAEvenAndNumBOdd()
NumAEvenOrNumBOdd()
