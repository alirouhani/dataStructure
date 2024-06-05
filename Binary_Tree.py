class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
                
class Binary_Tree:
    def __init__(self):
        self.root = None
        self.i = 0
        
    def setRoot(self, value):
        self.root = Node(value)
        self.i += 1

    def find(self, value, node = None):
        if node == None:
            node = self.root
        if node.val == value:
            return node
        if node.left != None:
            x = self.find(value, node.left)
            if x != None:
                return x
        if node.right != None:
            y = self.find(value, node.right)
            if y != None:
                return y

    def add(self, parent_value, value):
        parent_node = self.find(parent_value)
        new_node = Node(value)
        new_node.parent = parent_node
        self.i += 1
        if parent_node.left == None:
            parent_node.left = new_node
        elif (parent_node.right == None):
            parent_node.right = new_node
        else:
            print("Current orintion is full!")

            
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
        if (node is None) or (node.left is None and node.left is None):
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
        
tree = Binary_Tree()
tree.setRoot(0)
tree.add(0, 2.66)
tree.add(0, 43.83)
tree.add(2.66, 45.34)
tree.add(43.83, 59.12)
print(tree.Preorder_Traversal())
