class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
                
class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.i = 0

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

    def MaxSelection(self, A: list):
        k = A[0]
        n = len(A)
        for i in range(1, n):
            if A[i] > k:
                k = A[i]
        return k

    def MinSelection(self, A: list):
        k = A[0]
        n = len(A)
        for i in range(1, n):
            if A[i] < k:
                k = A[i]
        return k

    def Inorder_Predecessor(self, node):
        A = self.Preorder_Traversal(node.left)
        m = self.MaxSelection(A)
        return self.find(m)

    def Inorder_Sucessor(self, node):
        A = self.Preorder_Traversal(node.right)
        m = self.MinSelection(A)
        return self.find(m)
    
    def add(self, value, node = None):
        if self.root is None:
            self.root = Node(value)
            self.i += 1
        else:
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

    def delete_left(self, value):
        node = self.find(value)
        if node.left is None and node.right is None:
            if node.val <= node.parent.val:
                node.parent.left = None
                node.parent = None
            else:
                node.parent.right = None
                node.parent = None
        elif (node.left != None) and (node.right != None):
            best_node = self.Inorder_Predecessor(node)
            check = 0
            if best_node.left != None:
                next_node = best_node.left.val
                best_node.left = None
                best_node.right = None
                check = 1
            if node.val <= node.parent.val:
                node.parent.left = best_node
                if best_node.parent.val != node.val:
                    best_node.parent.right = None
                    best_node.left = node.left
                    best_node.left.parent = best_node                    
                else:
                    best_node.left = None
                best_node.parent = node.parent
                best_node.right = node.right
                best_node.right.parent = best_node                   
            else:
                node.parent.right = best_node
                if best_node.parent.val != node.val:
                    best_node.parent.right = None
                    best_node.left = node.left
                    best_node.left.parent = best_node                    
                else:
                    best_node.left = None
                best_node.parent = node.parent
                best_node.right = node.right
                best_node.right.parent = best_node                
            if check == 1:
                self.add(next_node)
        else:
            if node.val <= node.parent.val:
                if node.left != None:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent                
            else:
                if node.left != None:
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent

    def delete_right(self, value):
        node = self.find(value)
        if node.left is None and node.right is None:
            if node.val <= node.parent.val:
                node.parent.left = None
                node.parent = None
            else:
                node.parent.right = None
                node.parent = None
        elif (node.left != None) and (node.right != None):
            best_node = self.Inorder_Sucessor(node)
            check = 0
            if best_node.right != None:
                next_node = best_node.right.val
                best_node.left = None
                best_node.right = None
                check = 1
            if node.val <= node.parent.val:
                node.parent.left = best_node
                if best_node.parent.val != node.val:
                    best_node.parent.left = None
                    best_node.right = node.right
                    best_node.right.parent = best_node                    
                else:
                    best_node.right = None 
                best_node.parent = node.parent
                best_node.left = node.left
                best_node.left.parent = best_node
            else:
                node.parent.right = best_node
                if best_node.parent.val != node.val:
                    best_node.parent.left = None
                    best_node.right = node.right
                    best_node.right.parent = best_node                                        
                else:
                    best_node.right = None
                best_node.parent = node.parent
                best_node.left = node.left
                best_node.left.parent = best_node                
            if check == 1:
                self.add(next_node)
        else:
            if node.val <= node.parent.val:
                if node.left != None:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent                
            else:
                if node.left != None:
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
    
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

    def Inorder_Traversal(self, node = None, reachable = None):
        if node == None:
            node = self.root
        if reachable == None:
            reachable = []
        if node.left != None:
            self.Inorder_Traversal(node.left, reachable)
        reachable.append(node.val)
        if node.right != None:
            self.Inorder_Traversal(node.right, reachable)
        return reachable

    def size(self):
        return self.i

    def isEmpty(self):
        if self.i == 0:
            return True
        else:
            return False

    def height(self, node):
        if (node is None):
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def isBalanced(self, node = None):
        if node == None:
            node = self.root
        lh = self.height(node.left)
        rh = self.height(node.right)
        if node.left is None:
            lb = True
        else:
            lb = self.isBalanced(node.left)
        if node.right is None:
            rb = True
        else:
            rb = self.isBalanced(node.right)
        if (abs(lh - rh) <= 1) and (lb is True) and (rb is True):
            return True
        else:
            return False

    def delete(self):
        node = self.root
        if (node.left != None) and (node.right != None):
            best_node = self.Inorder_Predecessor(node)
            check = 0
            if best_node.left != None:
                next_node = best_node.left.val
                best_node.left = None
                best_node.right = None
                check = 1
            if best_node.parent.val != node.val:
                best_node.parent.right = None
                best_node.left = node.left
                best_node.left.parent = best_node
            else:
                best_node.left = None
            best_node.parent = node.parent          
            best_node.right = node.right  
            best_node.right.parent = best_node
            self.root = best_node
            if check == 1:
                self.add(next_node)
        else:
            if node.left != None:
                node.left.parent = None
                node.left = None
            if node.right != None:
                node.right.parent = None
                node.right = None
                
        
bst = Binary_Search_Tree()
bst.add(7)
bst.add(9)
bst.add(10)
bst.add(4)
bst.add(1)
bst.add(5)
bst.add(2)
bst.add(8)
bst.add(6)
bst.add(3)
bst.add(12)
bst.add(11)
print(bst.Postorder_Traversal())
bst.delete_left(9)
print(bst.Postorder_Traversal())
print(bst.isBalanced())
print(bst.root.val)
