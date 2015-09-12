def maxProduct(nums):
    #find max negative product and max positive product respectively
    #if the last neg product*cur turns into a positive one -> update the positive prd
    #if last pos product*cur turns into a neg one ->update negative    
    maxP=nums[0]
    tmp=1
    tmp_=1
    for i in nums: 
        if i<0:
            
            if tmp_<0:
                a=tmp
                tmp = tmp_*i
                maxP=max(maxP,tmp_*i)
                tmp_=min(a*i,i)
            else:
                tmp_=tmp_*i
                tmp=1
        if i==0:
            tmp=1
            tmp_=1
            maxP=max(0,maxP)
        if i >0:
            tmp=tmp*i
            tmp_=tmp_*i
            maxP=max(maxP,tmp)
    return maxP
