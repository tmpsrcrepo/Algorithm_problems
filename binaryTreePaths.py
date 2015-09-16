def binaryTreePathFind(root,path,result):
    if root == None:
        return 
    path=path+'->'+str(root.val)
    if root.left==None and root.right==None:
        result.append(path)
    else:
        binaryTreePathFind(root.left,path,result)
        binaryTreePathFind(root.right,path,result)
        #backtrack (move up)
        path=path[:-1]
        
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        binaryTreePathFind(root,'',result)
        return map(lambda x:x[2:],result)
