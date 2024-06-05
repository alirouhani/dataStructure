class Array_Binary_Tree:
    def __init__(self, max_size):
        self.n = (2 ** max_size) - 1
        self.i = 0
        self.x = [None] * self.n
        
    def setRoot(self, value):
        self.x[0] = value
        self.i += 1

    def find(self, value):
        for i in range(self.i):
            if self.x[i] == value:
                return i

    def add(self, parent, value):
        if self.i + 1> self.n:
            print("Array is full!")
        else:
            i = self.find(parent)
            if self.x[2*i + 1] == None:
                self.x[2*i + 1] = value
                self.i += 1
            elif (self.x[2*i + 2] == None):
                self.x[2*i + 2] = value
                self.i += 1
            else:
                print("Current orintion is full!")

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
        return self.x[2 * i + 1], self.x[2 * i + 2]
    
tree = Array_Binary_Tree(4)
tree.setRoot("Bashiri")
tree.add("Bashiri", "Nikzad")
tree.add("Bashiri", "Minaei")
tree.add("Nikzad", "Jalilvand")
tree.add("Minaei", "Rahmati")
tree.add("Nikzad", "Mousavi")
tree.add("Minaei", "Golkarian")
tree.add("Mousavi", "PRP")
print(tree.show())
print(tree.find_parent("Rahmati"))
print(tree.find_child("Mousavi"))
