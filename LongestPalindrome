#based on https://leetcode.com/discuss/32204/simple-c-solution-8ms-13-lines
def longestPalindrome(self,s):
    lim = len(s)
    if lim <= 1:
        return s
    start = 0
    maxLen = 1
    
    i = 0
    while i < lim-1:
        if lim-i<=maxLen/2:
            break
        j = k = i
        while k<lim-1 and s[k+1]==s[k]: #skip duplicate characters
            k+=1
        i = k+1
        while k<lim-1 and j>0 and s[k+1]==s[j-1]:#find palindrome: outside of duplicate characters
            k+=1
            j-=1
        newLen = k-j+1
        if newLen > maxLen:
            start = j
            maxLen = newLen
    return s[start:start+maxLen]
