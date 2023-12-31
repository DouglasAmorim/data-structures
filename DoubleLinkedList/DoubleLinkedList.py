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
    
    def get(self, index): 
        if index < 0 or index >= self.length: 
            return None
        
        if index < (self.length/2):
            temp = self.head
            for _ in range(index): 
                temp = temp.next
            return temp
        else: 
            temp = self.tail
            for _ in range(self.length - 1, index, -1): 
                temp = temp.prev
            return temp
    
    def set_value(self, index, value): 
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
        

        newNode = Node(value)
        before = self.get(index - 1)
        after = before.next

        before.next = newNode
        newNode.prev = before
        newNode.next = after

        if after is not None: 
            after.prev = newNode

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

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    
myDoublyLinkedList = DoublyLinkedList(7)
myDoublyLinkedList.append(2)
myDoublyLinkedList.append(5)
myDoublyLinkedList.append(9)
myDoublyLinkedList.set_value(1, 456)
myDoublyLinkedList.insert(4, 4)
myDoublyLinkedList.remove(1)
#myDoublyLinkedList.prepend(15)
#myDoublyLinkedList.pop()
#myDoublyLinkedList.pop_first()
myDoublyLinkedList.print_list()
#print(myDoublyLinkedList.get(3).value)