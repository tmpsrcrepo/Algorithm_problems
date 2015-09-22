class permuteUniqueSolution(object):
  #another version (similar logic, more concise)
    def permute(self,nums,tmp,res):
        if not nums:
            res.append(tmp)
        
        for i in xrange(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            self.permute(nums[:i]+nums[i+1:],tmp+[nums[i]],res)
                    
    def permuteU_(self,nums,pos,prev,tmp,res):
        if len(tmp)==pos:
            res.append(tmp)

        else:
            for i in range(0,len(nums)):
                if prev!=nums[i]:
                    self.permuteU_(nums[:i]+nums[i+1:],pos,prev,tmp+[nums[i]],res)
                    prev = nums[i]
                else:
                    self.permuteU_(nums[i+1:],pos,prev,tmp+[nums[i]],res)
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        prev = nums[0]-1
        self.permuteU_((nums),len(nums),prev,[],res)
        #self.permute(nums,[],res)
        return res
        
