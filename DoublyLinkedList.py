class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        new_node = Node(value)
        if self.length < 1:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        elif self.length == 1:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
            self.length -= 1
        return True
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
        






my_dll = DoublyLinkedList(7)
my_dll.append(435)
my_dll.append(435)
my_dll.prepend(35)
my_dll.pop()
my_dll.print_list()