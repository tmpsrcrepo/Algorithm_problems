class Permutation_Solution(object):
    def permute_(self,nums,pos,tmp,res):
        if len(nums)==0:
            res.append(tmp)
        else:
            for i in range(0,len(nums)):
                self.permute_(nums[:i]+nums[i+1:],i,tmp+[nums[i]],res)
    def permute(self, nums):
        res = []
        self.permute_(nums,0,[],res)
        return res
