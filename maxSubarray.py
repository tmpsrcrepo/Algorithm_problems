def maxSubArray(nums):
    prv = nums[0]
    temp = nums[0]
    for i in range(1,len(nums)):
        temp+=nums[i]
        #update the max sum if temp sum is greater than max
        prv = max(prv,temp)
        if temp<nums[i]:                
            temp=nums[i]    
    return prv
