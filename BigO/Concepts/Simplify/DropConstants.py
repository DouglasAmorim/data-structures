
# This codes O(2n) but we can simplify and call O(n)
# Doesnt matter if was O(100n) O(1000n) is always O(n)
def print_items(n): 
    for i in range(n): 
        print(i)

    for j in range(n): 
        print(j)

print_items(10)