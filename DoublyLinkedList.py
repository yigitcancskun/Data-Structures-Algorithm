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
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        temp.next = None
        temp.prev = None
        before.next = after
        after.prev = before
        
        self.length -= 1
        return True
    







my_dll = DoublyLinkedList(7)
my_dll.append(3)
my_dll.append(5)
my_dll.insert(2,343)
my_dll.append(4)
my_dll.prepend(35)
my_dll.pop_first()
my_dll.pop()
my_dll.print_list()