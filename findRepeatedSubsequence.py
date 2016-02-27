def findRepeatedDnaSequences(self, s, k):
    # k = fixed length of subsequence 
    #find subsequences in length of k which appears more than once in a sequence, s
    lim = len(s) - k - 1
    hashtable = collections.defaultdict(int)
    out = []
    for i in xrange(lim):
        subseq = s[i:i+10]
        hashtable[subseq]+=1
        if hashtable[subseq]==2:
            out.append(subseq)
    
    
    
    return out
