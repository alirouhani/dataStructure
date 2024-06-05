class DoubleEndedQueue:
    def __init__(self, max_size):
        self.n = max_size
        self.x = [0] * max_size
        self.i = 0
        self.f = 0

    def show(self):
        return self.x
        
    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

    def front(self):
        return self.x[self.f]

    def rear(self):
        return self.x[(self.i + self.f - 1) % self.n]

    def add_front(self, a):
        if self.i >= self.n:
            print("I'm so sorry, I can't do it.")
        else:
            self.x[(self.i + self.f) % self.n] = a
            self.i += 1

    def add_rear(self, a):
        if self.i >= self.n:
            print("I'm so sorry, I can't do it.")
        else:
            self.f =(self.f -1) % self.n
            self.x[self.f ] = a
            self.i += 1

    def remove_rear(self):
        if self.i == 0:
            print("I can't do this operation!")
        else:
            p = self.x[self.f]
            self.x[int(self.f)] = 0
            self.f = (self.f + 1) % self.n
            self.i -= 1
            return p

    def remove_front(self):
        if self.i == 0:
            print("I can't do this operation!")
        else:
            self.i -= 1
            p = self.x[(self.i + self.f ) % self.n]
            self.x[(self.i + self.f) % self.n] = 0
            return p

n=input()
deq=DoubleEndedQueue(int(n))
deq.add_front(1)
print(deq.show())
deq.add_front(8)
print(deq.show())
deq.add_rear(3)
print(deq.show())
deq.add_front(2)
print(deq.show())
deq.add_rear(5)
print(deq.show())
print("front is: {}".format(deq.front()))
print("rear is: {}".format(deq.rear()))
print("size is: {}".format(deq.size()))
print(deq.isEmpty())
print(deq.remove_front())
print(deq.remove_rear())
print(deq.remove_rear())
print(deq.remove_front())
print(deq.show())
