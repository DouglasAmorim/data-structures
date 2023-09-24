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
        self.length = 1

    def printList(self): 
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next

    def append(self, value): 
         # Create a new node 
         # and add that node to the end
        newNode = Node(value)

        if self.head is None: 
            self.head = newNode
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        
        return True
    
    def pop(self): 
        if self.head is None: 
            return None
        
        temp = self.head
        pre = self.head

        while (temp.next): 
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value): 
         # Create a new node 
         # and add that node to the beginning
        pass

    def insert(self, index, value):
        # Create a new node 
        # insert a node
        pass

myLinkedList = LinkedList(4)
#myLinkedList.append(3)
#myLinkedList.append(1)
#myLinkedList.pop()
myLinkedList.pop()
print(myLinkedList.printList())