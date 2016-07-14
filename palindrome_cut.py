'''
Minimum number of palindrome cuts
extremely classic DP questions:
need two DP concepts to make this work:
1. dp[i]= min(dp[j-1]+1,dp[i]) -> calculate the best cut
2. however TLE occurs for strings like "aaaaaaaaaaaaaaaaaab"
3. in order to avoid repetitively check palindromes of previous states, needs to memorize the status of palindrome: 
use PalindromeStatus[j][i] to memorize the if substring s[j:i+1] is a palindrome
4. this is still not enough, to further speed up, we need to use the property of palindrome:
new palindrome = s[i] + old palindrome + s[j] if s[i]=s[j]
therefore, we just need to check if substring from (j+1) to (i-1) is a palindrome

another case for palindrome is: aa. so if i-j == 1 -> another case of palindrome

'''

class Solution(object):
    def minCut(self, s):
        #state = minimum count at each location
        lim = len(s)
        if lim == 0:
            return 0
        
        dp = [lim]*(lim)
        #key of the problem: to save the palindrome status in order to avoid 
        #repeated check (since each check takes O(k))
        
        #status: [j,i]: if substring from j to i is a palindrome
        PalindromeStatus= [[False for i in xrange(lim)] for j in xrange(lim)]
        PalindromeStatus[0][0] = True

        for i in xrange(lim):
            #tmp = i
            #first mark [i][i] as palindrome
            PalindromeStatus[i][i] = True
            #check if the first i letter can be a palindrome
            # s[0]+s[1:i]+s[i] can be a palindrome
            if s[0]==s[i] and (i<=1 or PalindromeStatus[1][i-1]):
                #PalindromeStatus[0][i] = True #not necessary
                dp[i] = 1
            else:
                for j in xrange(1,i+1):
                    #very important:
                    #if s[i]=s[j]: s[i]+old palindrom+s[j] = new palindrome
                    #or s[i]+s[j] itself is a palindrome
                    if s[i] == s[j] and (i-j<=1 or PalindromeStatus[j+1][i-1]==True):
                        #print i,j, s[j-1:i],dp
                        dp[i]= min(dp[j-1]+1,dp[i])
                        PalindromeStatus[j][i] = True
        
        
        return dp[-1]-1
        
        
