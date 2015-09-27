# Question: to find a,b,c where sum(a,b,c) = 0 and a<b<c
# Solution: 
        """
        Since a+b+c = 0 and a<=b<=c
        Then there're only two cases: 
        1. a+b < 0, c > 0
           -> Case 1: a<0, b=0, c=-a
           -> Case 2: a<0, b>0, c>0
           -> Case 3: a<0, b<0, c>0
        2. a+b = 0, c = 0,
           however, b can't be greater than 0 since c = 0
           -> Case 4: a=0, b=0, c = 0
        
        c can only be >=0. dict_pos will store positive and zero candidates
        b and c can only be <=0. dict_neg will store negative candidates
        zeros = count(zeros)
        
        After defining the domain of each solution, we traverse the sorted array once to populate dictionaries
        if we find 3 zeros, then we append (0,0,0) immediately
        then we traverse dict_neg and use the method of solving 2sum (find a,b where a+b = c)
        now target value = -1*current value (=sum of the other two)
        then we traverse dict_pos and find if any case 1 and 2 can be found
                 for case 3, we can check its exisitence in dict_neg 
        """
        
def threeSum(nums):
    # dictionary for positive and negative values
    dict_pos = {}
    dict_neg = {}
    zeros = 0
    result = []
    nums = sorted(nums)
    for i in range(0,len(nums)):
        val = nums[i]
        if val < 0:
            if val in dict_neg:
                dict_neg[val].append(i)
            else:
                dict_neg[val]=[i]
        elif val == 0:
            zeros+=1
        else:
            if val in dict_pos:
                dict_pos[val].append(i)
            else:
                dict_pos[val]=[i]       
    if zeros > 2:
        result.append([0,0,0])

    for a in dict_neg:
        target = -a
        for k,v in dict_pos.items():
            find = target -k 
            if find == 0:
                if zeros > 0:
                    result.append([a,0,k])         
            elif find == k:
                if len(v)>1:
                    result.append([a,k,k])
            elif find > 0:
                if find < k:
                    if dict_pos.__contains__(find):
                        result.append([a,find,k])
                    
            else:
                if dict_neg.__contains__(find):
                    if find == a:
                        if len(dict_neg[a])>1:
                            result.append([a,a,k])
                    if find > a:
                        result.append([a,find,k])
    return result
 
