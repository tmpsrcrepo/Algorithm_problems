class minWindowSubstring(object):
    '''
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
    '''
    def minWindow(self, source, target):
        
        start = end = 0
        wordDict = collections.defaultdict(int)
        counter = 0
        for t in target:
            wordDict[t]+=1
            counter+=1
        #counter = len(t)
        lim = len(source)
        minLen=sys.maxint
        outStart=outEnd = 0
        
        
        while end < lim:
            if wordDict[source[end]] > 0:
                
                counter-=1
            wordDict[source[end]]-=1
            
            while counter == 0:
                tmpLen = end - start
                if tmpLen < minLen:
                    minLen = tmpLen
                    outStart,outEnd = start,end
                
                wordDict[source[start]]+=1
                if wordDict[source[start]]>0:
                    counter+=1
                start+=1
            end+=1
            #print wordDict,source[outStart:outEnd+1],counter
        
        if minLen == sys.maxint:
            return ''
        return source[outStart:outEnd+1]
