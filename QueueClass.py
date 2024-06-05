class Queue:
    def __init__(self, max_size):
        self.n = max_size
        self.x = [0] * max_size
        self.i = 0
        self.f = 0

    def show(self):
        return self.x

    def enqueue(self, a):
        if self.i >= self.n:
            print("Queue is full.")
        else:
            self.x[(self.i + self.f) % self.n] = a
            self.i += 1
        

    def dequeue(self):
        if self.i == 0:
            print("Queue is empty.")
        else:
            p = self.x[self.f]
            self.x[int(self.f)] = 0
            self.f = (self.f + 1) % self.n
            self.i -= 1
            return p
        
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
        return self.x[self.i]
        
n=input()
q=Queue(int(n))
q.enqueue("hi")
print(q.i)
q.enqueue(3)
q.enqueue(True)
print(q.i)
print(q.show())
o=q.dequeue()
print(o)
print(q.i)
print(q.rear())
print(q.front())
print(q.show())
