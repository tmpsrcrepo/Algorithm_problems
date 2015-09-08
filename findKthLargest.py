#using partition in quicksort to find kth largest (i.e. (n-k) smallest)
def findKth(nums,l,h,k):
    if nums:
        pivot_index = partition(nums,l,h)
        if k == (pivot_index+1):
            #find kth smallest
            return nums[pivot_index]
        if k < (pivot_index+1):
            return findKth(nums,l,pivot_index-1,k)
        return findKth(nums,pivot_index+1,h,k)
            
