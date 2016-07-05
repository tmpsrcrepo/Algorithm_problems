#Two pointers + Hashmap
class minWindowSubstring(object):
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
            #if the character is not visited (or visited but outside the window)
            #decrement the counter
            
            #expand the right side of the window (if not all of the characters are included)
            c = source[end]
            if wordDict[c] > 0:
                counter-=1
            #if the character is visited and in t: wordDict[c] < 0
            #if the charcter is not in t: wordDict[c] = 0
            wordDict[c]-=1
            
            
            #find the left side of the window when all of the characters are included
            while counter == 0:
                tmpLen = end - start
                if tmpLen < minLen:
                    minLen = tmpLen
                    outStart,outEnd = start,end
                #increment the count in dictionary
                wordDict[source[start]]+=1
                #if the count is greater than 0, decrement the count
                if wordDict[source[start]]>0:
                    counter+=1
                start+=1
            end+=1
            #print wordDict,source[outStart:outEnd+1],counter
        
        if minLen == sys.maxint:
            return ''
        return source[outStart:outEnd+1]
