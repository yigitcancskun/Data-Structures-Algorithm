class Node:
    def __init__(self, value): # creating a nod
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            return temp

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            print("Appended:", value)
            return value





my_linked_list = LinkedList(5)
print(my_linked_list.head.value)  # Output: 4
my_linked_list.append(10)
my_linked_list.append(10)

my_linked_list.append(10)
my_linked_list.append(10)
my_linked_list.print_list()  # Output: 4 -> 10