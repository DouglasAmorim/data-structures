class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        newNode = Node(value)
        self.root = newNode

    def __init__(self): 
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root is None: 
            self.root = newNode
        else:
            temp = self.root
 
            while temp is not None: 
                if temp.value < newNode.value: 
                    if temp.right is None: 
                        temp.right = newNode
                        return True
                    temp = temp.right
                elif temp.value > newNode.value: 
                    if temp.left is None: 
                        temp.left = newNode
                        return True
                    temp = temp.left
                else: 
                    return False
            
            temp = newNode
            
        return True

my_tree = BinarySearchTree()
my_tree.insert(3)

print(my_tree.root)