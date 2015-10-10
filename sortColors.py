
def sortColors(self, nums):
      """
      :type nums: List[int]
      :rtype: void Do not return anything, modify nums in-place instead.
      """

      i = 0
      j = len(nums)-1
      flag = 0
      while i<j:
          if nums[i] == 0:
              i+=1
          elif nums[i] == 1:
              if flag == 0:
                  tmp = i
                  while nums[tmp]==1 and tmp<j:
                      tmp+=1
                      if tmp == j:
                          flag = 1
                  nums[i],nums[tmp] = nums[tmp],nums[i]
              else:
                  i+=1
          else:
              while nums[j] >= 2 and j>i:
                  j-=1
              nums[i],nums[j] = nums[j],2

              j-=1
