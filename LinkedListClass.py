class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

    def get_ID(self):
        a=self.val
        b=self.next.val
        c=self.prev.val
        return a, b, c

class LinkedList:
    def __init__(self):
        self.r = Node(None)
        self.r.next = self.r
        self.r.prev = self.r
        self.i = 0

    def add_node(self, prev_node, value):
        new_node = Node(value)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.next.prev = new_node
        self.i +=1

    def delete_node(self, node):
        self.i -=1
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self,ind):
        if ind >=  self.size(): 
            print('Out of list')
        else:
            x = self.r.next
            for i in range(ind) :
                x=x.next
            return x

    def find(self, val):
        x = self.r.next
        for i in range(self.size()) :
            if x.val == val :
                return x
            x=x.next
        return None

    def display(self, ind):
        x=self.get(ind)
        node_id=x.get_ID()
        return node_id

    def show(self):
        s = [0] * self.i
        cur = self.r.next
        for i in range(self.i):
            s[i] = cur.val
            cur = cur.next
        return s
        
    def size(self):
        return self.i
      
    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False


link=LinkedList()
link.add_node(link.r,"hi")
link.add_node(link.find("hi"),3)
link.add_node(link.get(0),"bashe")
print(link.display(0))
print(link.display(1))
print(link.display(2))
link.delete_node(link.get(1))
print(link.display(0))
print(link.display(1))
print(link.show())
print(link.get(0))
