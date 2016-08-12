'''
General template for solving K sum problem. 
Note: finding list of sums -> not counting (otherwise we can just use 2d array and apply DP)

Recursively solve the problem until reach the base case: k = 2 and then use  the 2 pointer approach
Inspired by this blog: http://www.sigmainfy.com/blog/summary-of-ksum-problems.html
'''

class K_sum:
    
    def twoPointer(self, nums, target, start, end, tmp_res, res):
        #print n
        
        while start < end:
            start_num = nums[start]
            end_num = nums[end]
            if start_num+end_num==target:
                res.append(tmp_res+[start_num,end_num])
                start+=1
            elif nums[start]+nums[end]<target:
                start+=1
            else:
                end-=1
    
    def kSum(self,A,k,target,start,end,tmp_res,res):
        #print k,start,end,target
        if start>=end:
            return
        if k == 2:
            self.twoPointer(A,target,start,end,tmp_res,res)
            #return
        else:
            for i in xrange(start,end-k+2):
                num = A[i]
                self.kSum(A,k-1,target-num,i+1,end,tmp_res+[num],res)
            
    def kSum_solver(self, A, k, target):
        res = []
        if k == 1:
            for a in A:
                if a == target:
                    res.append([a])
            return res
        
        vA = sorted(A)
        self.kSum(A,k,target,0,len(A)-1,[],res)
        return res
