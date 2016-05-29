class woodCut_solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        #binary search to find the candidate
        if not L:
            return 0
        
        min_ = lmin = 1
        max_ = lmax = max(L)
        
        median = 0 #max length
        count = 0
        res = 0
        
        
        #corner case: if k is too large (or inplausible)
        if sum(L) < k:
            return 0
        
        while lmin <= lmax:
            median = (lmin+lmax)/2
            count = sum([l/median for l in L])

            if count < k: #cut size is too big, find the cut size in the first half
                lmax = median
            elif median > res:
                res = median
                lmin = median
            else:
                return res
                
                
        
        
        return 0
