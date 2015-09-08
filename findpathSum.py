#path sum II: return all possible paths
def findPathSum(root,sum_,path,result):
    if root == None:
        return
        
#    pathsum+=root.val
    path.append(root.val)
    if root.left==None and root.right==None and root.val==sum_:
        result.append(path)
        return

    else:
        findPathSum(root.left,sum_-root.val,path[:],result)
        findPathSum(root.right,sum_-root.val,path[:],result)
    

def pathSum(root,sum):
    result = []
    findPathSum(root,sum,[],result)
    return result
