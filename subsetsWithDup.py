class subsetswithDupSolution(object):
    def subsetsIterative(self,nums):
        nums = sorted(nums)
        result = [[],[nums[0]]]
        tmpresult = results[-1]
        prev = nums[0]
        if len(nums)>1:
            for i,n in enumerate(nums[1:]):
                if prev!=n:
                    prev = n
                    tmpresult=[]
                    for res in result:
                        tmpresult.append(res+[n])
                else:
                    tmpresult = [tmp+[n] for tmp in tmpresult]
                result+=(tmpresult)
        return result
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsIterative(nums)
