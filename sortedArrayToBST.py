def buildBST(nums,start,end):
    if start <= end:
        mid_pt = start+(end-start)/2
        tmp = TreeNode(nums[mid_pt])
        tmp.left = buildBST(nums,start,mid_pt-1)
        tmp.right = buildBST(nums,mid_pt+1,end)
        return tmp

    
def sortedArrayToBST(nums):
    return buildBST(nums,0,len(nums)-1)
        
