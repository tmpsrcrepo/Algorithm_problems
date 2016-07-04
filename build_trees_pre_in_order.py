#very similar to "build trees from post and in-order"
#the key is: list out two orders and observe
# pre order: find the root
# in order: left tree and right tree (two halves divided by the pivot point
# optimization: use hash table to memorize the index of each value
class build_trees_pre_in_order(object):
    def build(self, preorder,pstart, inorder, start, end,dict_locs):
        if start < end:
            #find the start node for the left tree, the next node
            value = preorder[pstart]
            tmpNode = TreeNode(value)
            #the next root location (searched in inorder), use dictionary to speed up
            i = dict_locs[value]
            
            
            #find the start node for the right tree: current node + size of left tree -> next right tree
            rstart = pstart+1+(i-start) 
            l = self.build(preorder,pstart+1,inorder,start,i,dict_locs)
            r = self.build(preorder,rstart,inorder,i+1,end,dict_locs)
            tmpNode.left = l
            tmpNode.right = r
            return tmpNode
        
    def buildTree(self, preorder, inorder):
        if preorder:
            dict_locs = {v:i for i,v in enumerate(inorder)}
            
            return self.build(preorder,0,inorder, 0, len(preorder),dict_locs)
            #return self.build(preorder,inorder)
