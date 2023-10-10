class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def print_stack(self): 
        temp = self.top

        while temp is not None: 
            print(temp.value)
            temp = temp.next

myStack = Stack(5)
myStack.print_stack()