class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList: 
    def __init__(self, value):
        # Create a new node 
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.lenght = 1

    def append(self, value): 
         # Create a new node 
         # and add that node to the end
        pass

    def prepend(self, value): 
         # Create a new node 
         # and add that node to the beginning
        pass

    def insert(self, index, value):
        # Create a new node 
        # insert a node
        pass

myLinkedList = LinkedList(4)

print(myLinkedList.head.value)