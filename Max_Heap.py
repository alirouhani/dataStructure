class Max_Heap:
    def __init__(self, max_size):
        self.n = (2 ** max_size) - 2
        self.i = 0
        self.x = [None] * self.n

    def find(self, value):
        for i in range(self.i):
            if self.x[i] == value:
                return i

    def add(self, value):
        import math
        if self.i + 1> self.n:
            print("Array is full!")
        else:
            i = self.i
            self.x[i] = value
            j = math.floor((i - 1) / 2)
            while self.x[j] != None and value > self.x[j]:
                temp = self.x[i]
                self.x[i] = self.x[j]
                self.x[j] = temp
                i = j
                j = math.floor((i - 1) / 2)
            self.i += 1

    def remove(self):
        j = 0
        i = self.i - 1
        temp = self.x[j]
        self.x[j] = self.x[i]
        self.x[i] = None
        k1, k2 = self.find_child(self.x[j])
        if k1*k2 != 0:
            i = self.find(max(k1, k2))
        elif (k1 != 0):
            i = self.find(k1)
        while k1 + k2 != 0 and self.x[i] > self.x[j]:
            temp = self.x[i]
            self.x[i] = self.x[j]
            self.x[j] = temp
            j = i
            k1, k2 = self.find_child(self.x[j])
            if k1*k2 != 0:
                i = self.find(max(k1, k2))
            elif (k1 != 0):
                i = self.find(k1)
        self.i -= 1
        return self.x
            
    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

    def show(self):
        return self.x

    def find_parent(self, value):
        import math
        i = self.find(value)
        return self.x[math.floor((i - 1) / 2)]

    def find_child(self, value):
        i = self.find(value)
        if (2 * i + 2) < self.n:
            if self.x[2 * i + 1] != None:
                x = self.x[2 * i + 1]
            else:
                x = 0
            if self.x[2 * i + 2] != None:
                y = self.x[2 * i + 2]
            else:
                y = 0
            return x, y
        else:
            return 0, 0

    def sort(self):
        l = self.i
        r = self.x
        u = self.x
        v = []
        while len(v) < l:
            v.append(u[0])
            u = self.remove()
        self.x = r
        self.i = l
        return v
    
tree = Max_Heap(4)
tree.add(34)
tree.add(29)
tree.add(25)
tree.add(56)
tree.add(10)
tree.add(48)
tree.add(5)
tree.add(31)
tree.add(32)
tree.add(42)
tree.add(19)
tree.add(45)
tree.add(15)
print(tree.show())
tree.remove()
print(tree.show())
print(tree.size())
print(tree.sort())
print(tree.show())
