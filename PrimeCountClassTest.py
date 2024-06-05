class Numbers:
    def __init__(self,value):
        self.x = value

    def isPrime(self):
        import math
        a = int(self.x)
        for i in range(2,math.floor(math.sqrt(a)+1)):
            if a%i==0:
                return False
            
        return True

    def PrimeCount(self):
        b=int(self.x)
        j=0
        a=[]
        for i in range(2,b):
            num=Numbers(i)
            if num.isPrime()==True:
                j+=1
                a.append(num.x)

        return j, a

n=input()
num1=Numbers(n)

print(num1.isPrime())
j, a=num1.PrimeCount()
print(j)
print(a)
