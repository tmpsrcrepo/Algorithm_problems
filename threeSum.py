
def threeSum(nums):
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
 
