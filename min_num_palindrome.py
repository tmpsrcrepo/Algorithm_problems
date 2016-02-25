def minCut(self, s):
    lim = len(s)
    dp = [lim]*(lim)
    dp[0]=1
    palindrome_state = [[False for i in xrange(lim)] for j in xrange(lim)] #memorize state in each substring(j,i) = palindrome
    palindrome_state[0][0] = True
    if not s:
        return 0
    for i in xrange(lim):
        palindrome_state[i][i]=True
        if s[0] == s[i] and (i<=1 or palindrome_state[1][i-1]):
            #palindrome_state[0][i]=True
            dp[i] = 1
        else:
            for j in xrange(1,i+1):
                if s[j]==s[i] and (i-j<=1 or palindrome_state[j+1][i-1]):
                    palindrome_state[j][i]=True
                    dp[i] = min(dp[i],dp[j-1]+1)
                    
    return dp[-1]-1
