class Simplex:
    def __init__(self, xcor, ycor, obj):
        self.x = xcor
        self.y = ycor
        self.z = obj

class Simplex_list:
    def __init__(self, max_size):
        self.n = max_size
        self.i = 0
        self.node_list = [0] * max_size

    def add(self, e: Simplex):
        newnode = e.z
        if self.i < self.n:
            self.i += 1
            j = self.i - 1
            while j > 0 and self.node_list[j-1].z < newnode:
                self.node_list[j] = self.node_list[j-1]
                j -= 1

            self.node_list[j] = e

    def remove(self, i):
        temp = self.node_list[i]
        for j in range(i,self.i-1):
            self.node_list[j] = self.node_list[j+1]
        self.node_list[self.i-1] = None
        self.i -= 1
        return temp.z
            
    def getZ(self, i):
        return self.node_list[i].z
    
l = Simplex_list(2)
l.add(Simplex(2.1,3.4,27.6))
l.add(Simplex(1.8,4.1,28.6))
print(l.getZ(0))
print(l.remove(0))
print(l.getZ(0))
