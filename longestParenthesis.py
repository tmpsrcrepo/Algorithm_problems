#the solution is pretty much similar to longest palindrome
# cache = []  (1d array, cache[i] = longest length from pos i)
# dp function to count: ()() and/or (()) 
def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s or s=='(':
        return 0
    
    start = 0
    lim = len(s)
    stack = []
    max_count = 0
    
    
    cache = [0 for i in xrange(lim)]
    
    while end<lim:
        p = s[end]
        if p == '(':
            stack.append(end)
        elif stack:
            index = stack.pop()
            cache[end] = 2
            cache[end]+=cache[max(0,index-1)]
            prev = end-1
            if prev-cache[prev]==index:
                cache[end]+=cache[prev]
                max_count = max(max_count,cache[end])
        end+=1
    return max_count
