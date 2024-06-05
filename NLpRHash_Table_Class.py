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
            j = self.hash(key + i ** 2)
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
                j = self.hash(key + i ** 2)
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
        i = 1
        j = self.hash(key + i ** 2)
        while self.k[j]!=0:
            if self.hash(self.k[j]) == self.hash(r):
                self.k[index] = self.k[j]
                self.v[index] = self.v[j]
                self.k[j] = 0
                self.v[j] = 0
                index = j
            i += 1
            j = self.hash(key + i ** 2)

    def remove(self, key):
        r, s, index = self.get(key)
        self.k[index] = 0
        self.v[index] = 0
        self.i -= 1
        
n = input()   
d=HashTable(int(n))
d.add(28, "hi")
d.add(15, "bye")
d.add(12, "salut")
d.add(41, "chao")
d.add(13, "hhhh")
d.add(42, "ok")
print(d.show())
d.delete(12)
print(d.show())
d.remove(28)
print(d.show())
print(d.size())
