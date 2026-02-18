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
    
    def pop_first(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
            self.length -=1
        return None
        
    # def get(self, index):
    #     if index < 0 or index > self.length:
    #         return None
    #     temp = self.head
    #     for _ in range(index):
    #         temp = temp.next
    #     return temp
    # this method for single linked list

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp.value
    







my_dll = DoublyLinkedList(7)
my_dll.append(3)
my_dll.append(5)
my_dll.append(4)
my_dll.prepend(35)
my_dll.pop_first()
my_dll.pop()
print(my_dll.get(2))
