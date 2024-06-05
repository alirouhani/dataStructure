class Node:
    def __init__(self, value, color):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
        self.uncle = None

class Red_Black_Tree:
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
    
    def add(self, value, node = None):
        if self.root is None:
            self.root = Node(value, "black")
            self.i += 1
        else:
            self.i += 1
            if node is None:
                node = self.root
            if node.val >= value:
                if node.left is None:
                    new_node = Node(value, "red")
                    new_node.parent = node
                    node.left = new_node
                    if node.parent != None:
                        if node.parent.left == node:
                            new_node.uncle = node.parent.right
                        else:
                            new_node.uncle = node.parent.left                        
                else:
                    self.add(value, node.left)
            else:
                if node.right is None:
                    new_node = Node(value, "red")
                    new_node.parent = node
                    node.right = new_node
                    if node.parent != None:
                        if node.parent.left == node:
                            new_node.uncle = node.parent.right
                        else:
                            new_node.uncle = node.parent.left                      
                else:
                    self.add(value, node.right)

    def recolor(self, node):
        if node.color == "black":
            node.color = "red"
        else:
            node.color = "black"
        return node.color

    def rotation(self, node):
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
                    if parent_node.parent != None:
                        node.uncle = parent_node.parent.right
                else:
                    if parent_node.parent != None:
                        node.uncle = parent_node.parent.right                    
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
                    if parent_node.parent != None:
                        node.uncle = parent_node.parent.left                    
                else:
                    parent_node.right = node
                    if parent_node.parent != None:
                        node.uncle = parent_node.parent.left                            
            else:
                node.parent = None
                
    def rearranging(self, node):
        if node.uncle == None or node.uncle.color == "black":
            main_node = node.val
            parent_node = node.parent.val
            grandparent_node = node.parent.parent.val            
            if (node.parent.left == node and node.parent.parent.left == node.parent) or (node.parent.right == node and node.parent.parent.right == node.parent):                
                self.rotation(node.parent)
                if node.parent.parent == None:
                    self.root = node.parent
                self.recolor(self.find(parent_node))
                self.recolor(self.find(grandparent_node))
            else:                
                self.rotation(node)
                self.rotation(node)
                if node.parent == None:
                    self.root = node
                self.recolor(self.find(main_node))
                self.recolor(self.find(grandparent_node))
        else:
            self.recolor(node.parent)
            self.recolor(node.uncle)
            if node.parent.parent != self.root:
                self.recolor(node.parent.parent)
                g_node = node.parent.parent
                if (g_node.color == g_node.parent.color and g_node.color == "red"):
                    return self.rearranging(g_node)


    def insert(self, value):
        self.add(value)    
        node = self.find(value)
        if node.parent != None and node.parent.color != "black":
            self.rearranging(node)      

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

    def family_finder(self, node):
        if node.parent != None:
            parent_node = node.parent
            if parent_node.left == node:
                if parent_node.right != None:
                    sibling = parent_node.right
                else:
                    sibling = None
                if sibling.right != None:
                    far_child = sibling.right
                else:
                    far_child = None                    
                if sibling.left != None:
                    near_child = sibling.left
                else:
                    near_child = None                     
            else:
                if parent_node.left != None:                
                    sibling = parent_node.left
                else:
                    sibling = None                    
                if sibling.left != None:
                    far_child = sibling.left
                else:
                    far_child = None                        
                if sibling.right != None:
                    near_child = sibling.right
                else:
                    near_child = None
            return parent_node, sibling, far_child, near_child

    def remove(self, value):
        del_node = self.find(value)
        if del_node.left is None and del_node.right is None:
            return self.case_a(del_node)
        elif (del_node.left != None) and (del_node.right != None):
            return self.case_b(del_node)                
        else:
            return self.case_c(del_node)
        
    def case_c(self, node):
        del_node = node
        if del_node.left != None:
            left_node = del_node.left
            del_node.val = left_node.val
            left_node.parent = None
            del_node.left = None
            if left_node.left != None:
                left_node.left.parent = del_node
                del_node.left = left_node.left
            if left_node.right != None:
                left_node.right.parent = del_node
                del_node.right = left_node.right              
        else:
            right_node = del_node.right    
            del_node.val = del_node.right.val
            right_node.parent = None
            del_node.right = None     
            if right_node.left != None:
                right_node.left.parent = del_node
                del_node.left = right_node.left
            if right_node.right != None:
                right_node.right.parent = del_node
                del_node.right = right_node.right          
                
    def case_b(self, node):
        del_node = node
        best_node = self.Inorder_Sucessor(del_node)
        if best_node.right != None:
            return self.case_c(best_node)
        else:
            return self.case_a(best_node, del_node)
                
    def case_a(self, del_node):
        value = best_node.val
        if best_node.color == "red":
            if best_node.val <= best_node.parent.val:
                best_node.parent.left = None
                best_node.parent = None
            else:                
                best_node.parent.right = None
                best_node.parent = None
            del_node.val = value
        else:                   
            return self.case_black(best_node)

    def case_black(self, node):                          
        if sibling != None and sibling.color == "black":
            if (sibling.left == None and sibling.right == None) or (sibling.left.color == "black" and sibling.right.color == "black"):
                print("ok")
                return self.case_b1(parent_node, sibling)
            elif far_child.color == "black":
                return self.case_b3(parent_node, sibling, far_child, near_child)
            elif far_child.color == "red":
                return self.case_b4(parent_node, sibling)
        elif (sibling != None and sibling.color == "red"):
            print("yes")
            print(parent_node.val)
            print(sibling.val)
            return self.case_b2(parent_node, sibling)        

    def case_b1(self, parent_node, sibling):
        if parent_node.color == "red":
            parent_node.color = "black"
            sibling.color = "red"
        else:
            sibling.color = "red"
            node = parent_node
            if node.parent != None:
                parent_node = node.parent
                if parent_node.left == node:
                    sibling = parent_node.right
                    far_child = sibling.right
                else:
                    sibling = parent_node.left
                    far_child = sibling.left                 
            return self.case_black(parent_node, sibling, far_child)

    def case_b2(self, parent_node, sibling):
        if parent_node.left == sibling and sibling.right != None:
            next_sibling = sibling.right
        if parent_node.right == sibling and sibling.left != None:
            next_sibling = sibling.left            
        col = parent_node.color
        parent_node.color = sibling.color
        sibling.color = col
        print("1: ", parent_node.color)
        print("2: ", sibling.color)
        print("3: ", next_sibling.val)
        print("4: ", next_sibling.color)         
        self.rotation(sibling)
        print("1: ", parent_node.val)        
        return self.case_black(parent_node, next_sibling)

    def case_b3(self, parent_node, sibling, far_child, near_child):
        col = sibling.color
        sibling.color = near_child.color
        near_child.color = col
        next_sibling = near_child        
        self.rotation(near_child)
        return self.case_b4(parent_node, next_sibling, far_child)
    
    def case_b4(parent_node, sibling, far_child):
        col = parent_node.color
        parent_node.color = sibling.color
        sibling.color = col
        self.rotation(sibling)
        self.recolor(self.find(far_child.val))
        
rbt = Red_Black_Tree()
rbt.insert(65)
rbt.insert(30)
rbt.insert(15)
rbt.insert(70)
rbt.insert(55)
rbt.insert(35)
rbt.insert(50)
rbt.insert(68)
rbt.insert(80)
rbt.insert(90)
rbt.insert(72)
rbt.insert(71)
rbt.insert(75)
print(rbt.Postorder_Traversal())
rbt.remove(65)
print(rbt.Postorder_Traversal())
print("=======")
print(rbt.find(70).color)
print(rbt.find(80).color)
print(rbt.find(90).color)
print("=======")
print(rbt.find(72).color)
print(rbt.find(75).color)
print(rbt.find(71).color)
print("=======")
#print(rbt.find(65).color)
print(rbt.find(68).color)
print(rbt.find(30).color)
print("=======")
print(rbt.find(50).color)
print(rbt.find(55).color)
print(rbt.find(35).color)
print(rbt.find(15).color)
