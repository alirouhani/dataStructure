class HashTable:
    def __init__(self, max_size):
        self.n = max_size
        self.k = [0] * max_size
        self.v = [0] * max_size
        self.i = 0

    def show(self):
        return self.k, self.v

    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

    def hash(self, key):
        return key % self.n
 
    def get(self, key):
        index = self.hash(key)
        check = 0
        for i in range(self.n):
            j = self.hash(key + i)
            if self.k[j] == key:
                check = 1
                return self.k[j], self.v[j], j
        if check != 1:
            print("Unknown Operation")
    
    def add(self, key, value):
        index = self.hash(key)
        if self.k[index] != 0:
            check = 0
            for i in range(self.n):
                j = self.hash(key + i)
                if self.k[j] == 0 and check == 0:
                    self.k[j] = key
                    self.v[j] = value
                    self.i += 1
                    check = 1
            if check == 0:
                print("Table is overflow")
        else:
            self.k[index] = key
            self.v[index] = value
            self.i += 1

    def delete(self, key):
        r, s, index = self.get(key)
        self.k[index] = 0
        self.v[index] = 0
        self.i -= 1

    def delete(self, key):
        r, s, index = self.get(key)
        self.k[index] = 0
        self.v[index] = 0
        self.i -= 1
        i = 1
        j = self.hash(key + i)
        while self.k[j]!=0 and i <= self.i:
            if self.hash(self.k[j]) == self.hash(r):
                self.k[index] = self.k[j]
                self.v[index] = self.v[j]
                self.k[j] = 0
                self.v[j] = 0
                index = j
            i += 1
            j = self.hash(key + i)

    def remove(self, key):
        r, s, index = self.get(key)
        self.k[index] = 0
        self.v[index] = 0
        self.i -= 1

        
d=HashTable(7)
d.add(28, "hi")
d.add(9, "bye")
d.add(12, "salut")
d.add(15, "chao")
d.add(42, "ok")
print(d.show())
d.delete(12)
print(d.show())
d.remove(28)
print(d.show())
print(d.size())
