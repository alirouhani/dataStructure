class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
                
class Splay_Tree:
    def __init__(self):
        self.root = None
        self.i = 0

    def MaxSelection(self, A: list):
        k = A[0]
        n = len(A)
        for i in range(1, n):
            if A[i] > k:
                k = A[i]
        return k

    def Inorder_Predecessor(self, node):
        A = self.Preorder_Traversal(node)
        m = self.MaxSelection(A)
        return self.find(m)

    def find(self, value, node = None):
        if node == None:
            node = self.root
        if node.val == value:
            return node
        if node.left != None and node.val >= value:
            x = self.find(value, node.left)
            if x != None:
                return x
        if node.right != None and node.val < value:
            y = self.find(value, node.right)
            if y != None:
                return y

    def Splay(self, node):
        while node.parent != None:         
            if node.parent.left == node:
                node.parent.left = node.right
                if node.right != None:                    
                    node.right.parent = node.parent
                parent_node = node.parent.parent        
                node.parent.parent = node           
                node.right = node.parent           
                if parent_node != None:
                    node.parent = parent_node
                    if parent_node.val >= node.val:
                        parent_node.left = node
                    else:
                        parent_node.right = node
                else:
                    node.parent = None    
            else:
                node.parent.right = node.left
                if node.left != None:                    
                    node.left.parent = node.parent
                parent_node = node.parent.parent            
                node.parent.parent = node
                node.left = node.parent
                if parent_node != None:               
                    node.parent = parent_node
                    if parent_node.val >= node.val:
                        parent_node.left = node
                    else:
                        parent_node.right = node                    
                else:
                    node.parent = None                
        self.root = node
                
    def add(self, value, node = None):
        if self.root is None:
            self.root = Node(value)
            self.i += 1
        else:
            self.i += 1
            if node is None:
                node = self.root
            if node.val >= value:
                if node.left is None:
                    new_node = Node(value)
                    new_node.parent = node
                    node.left = new_node
                else:
                    self.add(value, node.left)
            else:
                if node.right is None:
                    new_node = Node(value)
                    new_node.parent = node
                    node.right = new_node
                else:
                    self.add(value, node.right)

    def insert(self, value):
        self.add(value)
        node = self.find(value)
        self.Splay(node)

    def search(self, value):
        node = self.find(value)
        self.Splay(node)

    def remove(self, value):
        node = self.find(value)
        self.Splay(node)
        right_node = node.right
        node.right.parent = None
        node.right = None
        node.left.parent = None
        node.parent = None
        self.root = node.left
        new_node = self.Inorder_Predecessor(node.left)
        self.Splay(new_node)        
        new_node.right = right_node
        right_node.parent = new_node
        
    def Postorder_Traversal(self, node = None, reachable = None):
        if node == None:
            node = self.root
        if reachable == None:
            reachable = []
        if node.left != None:
            self.Postorder_Traversal(node.left, reachable)
        if node.right != None:
            self.Postorder_Traversal(node.right, reachable)
        reachable.append(node.val)
        return reachable

    def Preorder_Traversal(self, node = None, reachable = None):
        if node == None:
            node = self.root
        if reachable == None:
            reachable = []
        reachable.append(node.val)
        if node.left != None:
            self.Preorder_Traversal(node.left, reachable)
        if node.right != None:
            self.Preorder_Traversal(node.right, reachable)
        return reachable
    
bst = Splay_Tree()
bst.insert(7)
bst.insert(9)
bst.insert(10)
bst.insert(4)
bst.insert(1)
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(6)
bst.insert(3)
bst.insert(12)
bst.insert(13)
print(bst.Postorder_Traversal())
bst.search(4)
print(bst.Postorder_Traversal())
bst.remove(6)
print(bst.Postorder_Traversal())
