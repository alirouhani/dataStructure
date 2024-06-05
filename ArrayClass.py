class Array:
    def __init__(self, max_size):
        self.n = max_size
        self.x = [0] * max_size
        self.i = 0

    def show(self):
        return self.x

    def add(self, a):
        if self.i+1>int(self.n):
            print("I can't do this operation! but I can resize the array.")
            q=input("If you want to resize the array, input 1. Otherwise 0: ")
            if int(q)==1:
                l=input("How much extra elements do you need? ")
                self.n=int(self.n)+int(l)
                temp=self.x
                self.x=[0]*int(self.n)
                for j in range(0,len(temp)):
                    self.x[j]=temp[j]
                    
                self.x[self.i]=a
                self.i +=1
        else:
                self.x[self.i]=a              
                self.i +=1
            
    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

    def find(self, value):
        for i in range(self.i):
            if self.x[i] == value:
                return i
        return None

    def remove(self, value):
        i = self.find(value)
        for j in range(i, self.i):
            self.x[j] = self.x[j + 1]
        return self.x
    
n=input()        
b=Array(int(n))
b.add("hi")
b.add(3)
b.add(8)
print(b.show())
b.add(2)
print(b.isEmpty())
print(b.size())
print(b.show())
print(b.n)
print(b.find(2))
print(b.remove(3))
