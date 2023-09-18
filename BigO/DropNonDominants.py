# The code above is O(nˆ2 + n)
# But Nˆ2 in that case is dominant, so we can represent as O(nˆ2)
def print_items(n): 
    # O(nˆ2)
    for i in range(n): 
        for j in range(n):
            print(i, j)

    # O(n)
    for k in range(n):
        print(k)
            
print_items(10)