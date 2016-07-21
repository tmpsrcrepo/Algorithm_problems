#given a dictionary of words, and a concatenated string -> see if it can be broken into a list of words

#Top down & bottm-up
class canBreak(object):
    #dp: state: cut by the current point: T/F/unvisited
    #backtrack: enumerate each character in the string
    def dfs(self,s,wordDict,index,dp):
        if index == len(s):
            return True
        if dp[index]!=-1:
            return dp[index]==1
        
        for i in xrange(index,len(s)):
            if s[index:i+1] in wordDict and self.dfs(s,wordDict,i+1,dp):
                return True
            
        dp[index] = 0
        return False
    def wordBreak(self, s, wordDict):
        dp = [-1]*len(s)
        for i,w, in enumerate(s):
            if s[:i+1] in wordDict:
                if dp[i]!=0 and self.dfs(s,wordDict,i+1,dp):
                    return True
        
        return False
    #backtrack: enumerate each word in the wordDict (this is the fastest solution)
    def dfs_word(self,s,wordDict,index,dp):
        if index == len(s):
            return True
        if dp[index]!=-1:
            return dp[index]==1
        
        for w in wordDict:
            l = len(w)
            if s[index:index+l]==w and self.dfs_word(s,wordDict,index+l,dp):
                return True
            
        dp[index] = 0
        return False

    def wordBreak(self, s, wordDict):
        dp = [-1]*len(s)
        return self.dfs_word(s,wordDict,0,dp)

    #bottom-up:
    def wordBreak(self,s,wordDict):
        lim = len(s)+1
        dp = [False]*(lim)
        last = 0
        for i in xrange(1,lim):
            if dp[i]==True or s[:i] in wordDict:
                dp[i] = True
                for j in xrange(i+1,lim):
                    if dp[j]==True or s[i:j] in wordDict:
                        dp[j]=True
                        
                    else:
                        dp[j] = False
            else:
                dp[i] = False
        #print dp
        return dp[-1]
