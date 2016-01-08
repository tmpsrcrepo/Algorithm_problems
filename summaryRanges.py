class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if len(nums)==0:
            return nums
        
        
        start = nums[0]
        start_str = str(start)
        out = [start_str]
        prev = start
        for a in (nums[1:]):
            if a-prev==1:
                out[-1]=start_str+'->'+str(a)
            else:
                start = a
                start_str = str(start)
                out.append(start_str)
            prev = a

        return out
            
    def summaryRangeDuplicates(self,nums):
        #duplicates
        if len(nums) == 0:
            return nums
        prev = start = nums[0]
        startstr = str(start)
        out = [startstr]
        for a in nums[1:]:
            if a-prev == 1 or a==prev:
                out[-1]=startstr+'->'+str(a)
            else:
                start = a
                startstr = str(start)
                out.append(startstr)
            prev = a
        return out
    
    
    def summaryRangesVaried(self,nums):
        #varied ranges
        if len(nums) == 0:
            return nums
        prev = start = nums[0]
        startstr =str(start)
        out = [startstr]
        diff = nums[1]-start
        diffstr = str(diff)
        len_ = len(nums)
        
        for i in xrange(1,len_):
            n = nums[i]
            tmp = n - prev
            if tmp == diff:
                out[-1] = startstr +'->' + str(n)+'/'+ diffstr
            else:
                diff = nums[min(i+1,len_-1)]-n
                diffstr = str(diff)
                start = n
                startstr = str(start)
                out.append(startstr)
            prev = n

        return out
        
