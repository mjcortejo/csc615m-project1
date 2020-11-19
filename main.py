from structure import Node, DoublyLinkedList

input_string = DoublyLinkedList()
input_string.append("#")
input_string.append("a")
input_string.append("b")
input_string.append("c")
input_string.append("#")
current = input_string.head

if current.data == "#":
    current = current.next

while (current.data != "#"):
    print(current.data)
    # last = current
    current = current.next