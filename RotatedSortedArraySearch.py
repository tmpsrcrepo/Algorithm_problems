class BS_RotatedArraySolution(object):
    def BSearch(self,nums,target,start,end):

        mid = (start+end)/2
        #print nums[start],nums[mid]
        if nums[mid] == target:
            return mid
        if start<end and nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if start > end:
            return -1
        if target < nums[mid]:
            if (nums[start] <= target) or (nums[start] > target and target<=nums[end] and nums[mid]<nums[end]):
                return self.BSearch(nums,target,start,mid-1)
        a = self.BSearch(nums,target,start,mid-1)
        if a == -1:
            return self.BSearch(nums,target,mid+1,end)
        return a

        

    def search(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
        
        if nums:
            return self.BSearch(nums,target,0,len(nums)-1)
