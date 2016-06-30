#count number of unique BST out of array [1...n]
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

def numTree(n):
    dp = [0]*(n+1)
    if n <= 2:
        return n
    dp[1] = 1
    dp[2] = 2
    
    for i in xrange(3,n+1):
        val = 0
        for j in xrange(1,i+1):
            val+= max(dp[j-1],1)*max(dp[i-j],1)
        dp[i]=val
    return dp[-1]
