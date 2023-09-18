# We cannot say this is a O(n) function, beacause are to differents parameters been used
# so this is O(a) + O(b), we can call O(a + b)
def print_items(a, b): 
    for i in range(a): 
        print(i)

    for j in range(b): 
        print(j)

# Following the same logic this will be O(a*b)
def print_items(a, b): 
    for i in range(a): 
        for j in range(b): 
            print(i,j)



print_items(10)