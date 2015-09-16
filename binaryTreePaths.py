
        
class Solution(object):
    def binaryTreePathFind(self,root,path,result):
    if root == None:
        return 
    path=path+'->'+str(root.val)
    if root.left==None and root.right==None:
        result.append(path)
    else:
        self.binaryTreePathFind(root.left,path,result)
        self.binaryTreePathFind(root.right,path,result)
        #backtrack (move up)
        path=path[:-1]
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.binaryTreePathFind(root,'',result)
        return map(lambda x:x[2:],result)
