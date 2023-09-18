# Only one operation is called O(1)
# Even thought we add another sum like (n + n + n) probably will be O(2), but we stand all O(1)
# also know as constant Time
def add_items(n): 
    return n + n

print(add_items(10))