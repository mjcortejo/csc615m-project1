from utils import create_case, simulator

def NumAEvenAndNumBOdd():
    print("NumAEvenAndNumBOdd")
    program = {
        '1': {'a': 1, '#': 'reject', 'b': 2, 'dir': 'right'},
        '2': {'a': 2, 'b': 1, '#': 3, 'dir': 'right'},
        '3': {'a': 3, 'b': 3, '#': 4, 'dir': 'left'},
        '4': {'a': 5, 'b': 4, '#': 'accept', 'dir': 'right'},
        '5': {'a': 4, 'b': 5, '#': 'reject', 'dir': 'right'}
    }
    cases = [
        create_case("#aabbb#"), #accept
        create_case("#aabb#"), #reject
        create_case("#baa#"), #accept
        create_case("#aaab#"), #reject
    ]

    simulator(cases, program)

def NumAEvenOrNumBOdd():
    print("NumAEvenOrNumBOdd")
    program = {
        '1': {'a': 1, 'b': 2, '#': 3, 'dir': 'right'},
        '2': {'a': 2, 'b': 1, '#': 'accept', 'dir': 'right'},
        '3': {'a': 3, 'b': 3, '#': 4, 'dir': 'left'},
        '4': {'a': 5, 'b': 4, '#': 'accept', 'dir':'right'},
        '5': {'a': 4, 'b': 5, '#': 'reject', 'dir': 'right'}
    }
    cases = [
        create_case("#aabbb#"), #accept
        create_case("#abb#"), #reject
        create_case("#baa#"), #accept
        create_case("#aaabb#"), #reject
    ]

    simulator(cases, program)

def NumAPlusNumBIsEven():
    print("NumAPlusNumBIsEven")
    program = {
        '1': {'a': 2, 'b': 2, '#': 'accept', 'dir': 'right'},
        '2': {'a': 1, 'b': 1, '#': 'reject', 'dir': 'right'}
    }
    cases = [
        create_case("#aabb#"), #accept
        create_case("#aaabb#"), #reject
        create_case("#baaba#"), #accept
        create_case("#babba#") #reject
    ]

    simulator(cases, program)

NumAEvenAndNumBOdd()
NumAEvenOrNumBOdd()
NumAPlusNumBIsEven()
