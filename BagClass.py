class Bag:
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

    def add(self, i, a):
        if i>=int(self.n):
            print("I can't do this operation! but I can resize the array.")
            q=input("If you want to resize the array, input 1. Otherwise 0: ")
            if int(q)==1:
                l=input("How much extra elements do you need? ")
                self.x=self.resize(self.x,l)    
                self.x[i]=a
                self.i +=1                
        else:
            if self.x[i]==0:
                self.x[i]=a
                self.i +=1                
            else:
                print("I can't do this operation!")
                print("Prevously you add '{}' into your array at this location.".format(self.x[i]))

            
    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

n=input()        
b=Bag(int(n))
b.add(0,"hi")
b.add(1,3)
b.add(2,8)
print(b.show())
b.add(0,2)
print(b.isEmpty())
print(b.size())
print(b.show())
print(b.n)
