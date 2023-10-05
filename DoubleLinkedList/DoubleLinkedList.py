class Node: 
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList: 
    def __init__(self, value): 
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def print_list(self):
        temp = self.head

        while temp is not None: 
            print(temp.value)
            temp = temp.next
    
    def append(self, value): 
        newNode = Node(value)

        if self.head == None: 
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
        return True
    
    def pop(self): 
        if self.length == 0: 
            return None
        else: 
            temp = self.tail

            if self.length == 1: 
                self.head == None
                self.tail == None
            else: 
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None

            self.length -= 1

            return temp
        
    def prepend(self, value): 
        newNode = Node(value)

        if self.head is None: 
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
        self.length += 1
        return True
    
    def pop_first(self): 
        if self.length == 0: 
            return None
        
        temp = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp
        
myDoublyLinkedList = DoublyLinkedList(7)
myDoublyLinkedList.append(2)
myDoublyLinkedList.append(5)
myDoublyLinkedList.append(9)
myDoublyLinkedList.prepend(15)
myDoublyLinkedList.pop()
myDoublyLinkedList.pop_first()
myDoublyLinkedList.print_list()