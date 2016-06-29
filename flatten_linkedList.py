# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #pre-order

    def traversal(self,root):
        if root:
            self.traversal(root.left)
            self.traversal(root.right)
            
            tmp = root.right
            root.right = root.left
            root.left = None
            #find the bottom of the right tree
            while root.right:
                root = root.right
            root.right = tmp
    def search(self,root,pre):
        if root:
            l = root.left
            r = root.right
            if pre:
                pre.right = root
                pre.left = None
            if l:
                root = self.search(l,root)
            if r:
                root  =self.search(r,root)
            return root
            
    def flatten(self, root):
        #self.traversal(root)
        pre  = None
        self.search(root,pre)
        
        #return head
        
