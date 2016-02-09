  """
  key idea: 2 queues, O(n)
  1 queue (or just a variable) to keep track where the window starts (and keep the queue size is no greater than k) 
  1 max_queue: pop elements from the queue if they're smaller than the current value, and retrieve the max value at O(1) cost
  
  """
  #method 1
  def maxSlidingWindow(self, nums, k):
      ans = []
      queue = []
      for i, v in enumerate(nums):
          if queue and queue[0] <= i - k:
              queue = queue[1:]
          while queue and nums[queue[-1]] < v:
              queue.pop()
          queue.append(i)
          if i + 1 >= k:
              ans.append(nums[queue[0]])
      return ans
  #method 2    
  def maxSlidingWindow1(self, nums, k):
      if len(nums) == 0:
          return []
      lim = len(nums)
      slidingWindow = [0]*(lim-k+1)
      
      #q = collections.deque([])
      #maxs = collections.deque([])
      #q = []
      last = nums[0]
      maxs = []
      count = 0
      
      for i,val in enumerate(nums):
          #pop from the front when len(q) == k
          if count == k:
              max_ = maxs[0]
              #q.popleft()
              #q = q[1:]
              #update the sliding window by the current max
              slidingWindow[i-k] = (max_)
              
              if max_ == last:
                  #maxs.popleft()
                  maxs = maxs[1:]
              last = nums[i-k+1]
              count-=1
              #print last

          #append elements on the queue & max queue
          #q.append(val)
          while len(maxs) > 0 and maxs[-1] < val:
              maxs.pop()
          maxs.append(val)
          count+=1

      slidingWindow[-1] = maxs[0]
      return slidingWindow
