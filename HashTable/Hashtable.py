class HashTable: 
    def __init__(self, size = 7): 
        self.data_map = [None] * size

    def __hash(self, key): 
        myHash = 0
        for letter in key: 
            myHash = (myHash + ord(letter) * 23) % len(self.data_map)
        return myHash
    
    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set(self, key, value): 
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key): 
        index = self.__hash(key)

        if self.data_map[index] is not None: 
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key: 
                    return self.data_map[index][i][1]
        
        return None
    
    def keys(self): 
        all_keys = []
        for i in range(len(self.data_map)): 
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

# This method is O(2n) so we drop the constant = O(n)
def item_in_common(list1, list2): 
    myDict = { }

    for i in list1: 
        myDict[i] = True

    for j in list2: 
        if j in myDict: 
            return True
    return False

list1 = [1,3,3] 
list2 = [2,4,6,5]
    
print(item_in_common(list1, list2))

myHashTable = HashTable()
myHashTable.set("emergency", 911)
myHashTable.set("call", 912)
myHashTable.set("the", 12)
myHashTable.set("police", 999)

print(myHashTable.get("teste"))
print(myHashTable.get("police"))
print(myHashTable.keys())
# myHashTable.print_table()