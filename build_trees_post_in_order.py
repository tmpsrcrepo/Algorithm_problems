
class builTreeFromPost_In_Order(object):
    #really similar to inorder and preorder: 
    #right tree root: the last second node in post order
    #left tree root: root - 1 - (size of right tree)   
    def build(self,postorder,post_end,inorder, in_start, in_end,dict_locs):
        if in_end >= in_start and post_end>=0:
            val = postorder[post_end]
            root = TreeNode(val)
            index = dict_locs[val]
            #find the new start point for the left subtree: start in postorder + size(left tree)
            cut_off = post_end - (in_end-index)
            
            l = self.build(postorder, cut_off-1, inorder, in_start, index-1, dict_locs)
            r = self.build(postorder,  post_end-1,  inorder, index+1, in_end,   dict_locs)
            root.left = l
            root.right = r
            return root
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            dict_locs = {v:i for i,v in enumerate(inorder)}
            return self.build(postorder,len(postorder)-1,inorder,0,len(inorder)-1,dict_locs)
        
