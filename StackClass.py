class Stack:
    def __init__(self, max_size):
        self.n = max_size
        self.x = [0] * max_size
        self.i = 0

    def show(self):
        return self.x

    def resize(self, prev_array, new_capacity):
        self.n = int(self.n)+int(new_capacity)
        temp = [0] * self.n
        for j in range(0,len(prev_array)):
            temp[j]=prev_array[j]
        return temp
    
    def push(self, a):
        if  self.i >= self.n:
            print("Overflow")
            q=input("If you want to resize the array, input 1. Otherwise 0: ")
            if int(q)==1:
                l=input("How much extra elements do you need? ")
                self.x=self.resize(self.x,l)    
                self.x[self.i]=a
                self.i +=1
        else:
            self.x[self.i] = a
            self.i +=1

    def pop(self):
        if self.i == 0:
            print("Underflow")
        else:
            self.i -=1
            p=self.x[self.i]
            self.x[int(self.i)]=0
            return p
        
    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

        
n=input()
s=Stack(int(n))
print(s.isEmpty())
s.push("premier")
s.push("2e")
s.push("dernier")
s.push(2)
s.push(5)
s.push(8)
print(s.show())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.show())
