#using partition in quicksort to find kth largest (i.e. (n-k) smallest)
def partition(nums,l,h):
    pivot = nums[h]
    i = l
    for j in range(l,h):
        if nums[j]<=pivot:
            #swap
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    nums[i],nums[h]=nums[h],nums[i] #next pivot
    return i
    
def findKth(nums,l,h,k):
    if nums:
        pivot_index = partition(nums,l,h)
        if k == (pivot_index+1):
            #find kth smallest
            return nums[pivot_index]
        if k < (pivot_index+1):
            return findKth(nums,l,pivot_index-1,k)
        return findKth(nums,pivot_index+1,h,k)
            
