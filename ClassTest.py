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


num1=Numbers(9)

print(num1.isPrime())
