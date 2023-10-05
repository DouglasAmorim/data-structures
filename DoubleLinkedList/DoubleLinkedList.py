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
        

myDoublyLinkedList = DoublyLinkedList(7)
myDoublyLinkedList.append(2)
myDoublyLinkedList.print_list()