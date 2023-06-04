class Node: 
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

#working BST constructor. 
# class BinarySearchTree:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.root=new_node

#With value none. When root is None. 
class BinarySearchTree:
    def __init__(self):
        self.root=None       

