class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        
        window = []
        maxLen = 1
        start = 0

        for i,a in enumerate(s):
            #check if there're more than 2 distinct characters
            if not window:
                window.append((a,i))
            elif window and window[-1][0]!= a:
                if a==window[0][0]:
                    window = window[1:]
                window.append((a,i))

            if len(window)>2:
                window = window[1:]
                start = window[0][1]
            maxLen = max(maxLen,i-start+1)
        return maxLen
