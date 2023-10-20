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


myHashTable = HashTable()
myHashTable.print_table()