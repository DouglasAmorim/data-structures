class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)
    
    def push(self, value): 
        self.stack_list.append(value)

    def pop(self):
        if self.size() == 0: 
            return None
        
        self.stack_list.pop()

def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()

def reverse_string(string): 
    stack = Stack()
    reversed_string = ""
 
    for char in string:
        stack.push(char)
 
    while not stack.is_empty():
        reversed_string += stack.pop()
 
    return reversed_string

myStack = Stack()
myStack.push(3)
print(reverse_string("banana"))
#myStack.pop()
myStack.print_stack()