def twoSum(nums,target):
        A = {}
        for i in range(0,len(nums)):
            val = nums[i]
            if A.__contains__(val):
                A[val].append(i)
            else:
                A[val]=[i]
        
        for k,v in A.items():
            if A.__contains__(target-k):
                if target-k==k:
                    if len(v)>=2:
                        return sorted([v[0]+1,v[1]+1])
                else:
                    return sorted([v[0]+1,A.get(target-k)[0]+1])
                    
