class Solution(object):
    def findDuplicate(self, nums):
        """
        use pigeon hole princeple: if we have more holes < pigeons, and 1 hole has at least 2 pigeons -> duplicate has been found
        
        #nums: [1,n], len = n+1
        use binary search to find the boundary b, which is smaller than number of elements smaller than b (duplicate in this region, otherwise it's in another part)
        """
        
        start = 0
        end = len(nums)-1
        
        while start < end:
            b = (start+end)/2
            count = sum([1 for i in nums if i <= b])
            if count > b:
                end = b
            else:
                start = b+1
        return start
