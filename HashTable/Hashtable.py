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


myHashTable = HashTable()
myHashTable.set("emergency", 911)
myHashTable.set("call", 912)
myHashTable.set("the", 12)
myHashTable.set("police", 999)
myHashTable.print_table()