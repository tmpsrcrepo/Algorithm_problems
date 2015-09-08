def numTree1(n):
    result = [1,1,2]
    itr = 0
    if n == 0:
        return 0
    elif n < 3:
        return result[n]
    else:
        for itr in range(3,n+1): 
            count = 0
            for i in range(1,itr+1):
                count += (result[itr-i]*result[i-1])
            result.append(count)
        return result[-1]
