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
        if self.k[index] == key:
            return self.k[index], self.v[index]
        else:
            print("Unknown operation")
            
    def add(self, key, value):
        index = self.hash(key)
        if self.k[index] != 0:
            q=input("If you want to overwrite the array, input 1. Otherwise 0: ")
            if int(q) == 1:
                self.v[index] = value
        else:
            self.k[index] = key
            self.v[index] = value
            self.i += 1

    def delete(self, key):
        index = self.hash(key)
        if self.k[index] == key:
            self.k[index] = 0
            self.v[index] = 0
            self.i -= 1
        else:
            print("Unknown operation")


n = input()        
d=HashTable(int(n))
d.add(28, "hi")
d.add(15, "bye")
d.add(12, "salut")
d.add(41, "chao")
r, s = d.get(41)
d.add(r, "ok")
print(d.show())
d.delete(28)
d.delete(3)
print(d.show())
print(d.size())
