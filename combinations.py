class Combinations_Solution(object):
    def ksubset_(self,nums,index,tmp,res,k):
    #
        if k == 0:
            res.append(tmp)
        else:
            for i in range(index,len(nums)):
                self.ksubset_(nums,i+1,tmp+[nums[i]],res,k-1)
                
    def combine(self, n, k):
        res = []
        self.ksubset_(range(1,n+1),0,[],res,k)
        return res
