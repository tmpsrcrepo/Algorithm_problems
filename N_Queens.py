class Solution(object):
    #out = 0
    def totalNQueens(self, n):
        if n == 1:
            return 1
        if n < 4:
            return 0
        res = [0]*n
        self.out = 0
        self.steps(n,0,res)
        return self.out
    
    def check(self,res,k):
        for i in xrange(0,k):
            if (res[i]==res[k]) or abs(res[i] - res[k])==(k-i):
                return False
        return True
    
    def steps(self,n,k,res):
        
        if k==n:
            self.out+=1
            return
        
        for q in xrange(0,n):
            res[k] = q
            if self.check(res,k):
                self.steps(n,k+1,res)

