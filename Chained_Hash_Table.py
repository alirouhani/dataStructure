class Node:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

    def get_ID(self):
        a=self.pair
        if self.next == None:
            return a, None
        else:
            b=self.next.pair
            return a, b

class Chained_HashTable():
    def __init__(self, max_size):
        self.n = max_size
        self.x = [None] * max_size
        self.i = 0

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
        cur = self.x[index]
        check = 0
        while check == 0:
            if cur.pair[0] == key:
                check = 1
                return cur.pair[1], cur.get_ID()
            else:
                if cur.next == None:
                    check = 1
                else:
                    cur = cur.next
        return -1

    def add(self, key, value):
        index = self.hash(key)
        if self.x[index] == None:
            self.x[index] = Node(key, value)
            self.i += 1
        else:
            check = 0
            cur = self.x[index]
            while check == 0:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    check = 1
                else:
                    if cur.next == None:
                        cur.next = Node(key, value)
                        check = 1
                        self.i += 1
                    else:
                        cur = cur.next

    def remove(self, key):
        index = self.hash(key)
        cur = self.x[index]
        if cur.pair[0] == key:
            self.x[index] = cur.next
            self.i -= 1
        else:
            check = 0
            prev = cur
            cur = cur.next
            while check == 0:
                if cur.pair[0] == key:
                    check = 1
                    self.i -= 1
                    prev.next = cur.next
                else:
                    if cur.next == None:
                        check = 1
                        return -1
                    else:
                        prev = cur
                        cur = cur.next

    def display(self):
        s = [0] * self.n
        for i in range(self.n):
            b = [0] * self.i
            if self.x[i] !=0:
                cur = self.x[i]
                j = 0
                while cur != None:
                    b[j] = cur.pair
                    cur = cur.next
                    j += 1
            s [i] = b
        return s

d=Chained_HashTable(5)
d.add(28, "hi")
d.add(15, "bye")
d.add(30, "bye0")
d.add(100, "b00919")
d.add(12, "salut")
d.add(41, "chao")
d.add(61, "ok")
d.add(51, "ok1")
print(d.get(51))
d.add(71, "ok2")
d.add(51, "let")
print(d.get(51))
print(d.get(15))
d.remove(30)
print(d.get(15))
print(d.size())
print(d.display())
