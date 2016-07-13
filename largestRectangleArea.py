class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        max_ = 0
        stack = []
        last_index = -1
        width = 0
        for i,h in enumerate(heights+[0]):
            while stack and h < heights[stack[-1]]:
                last_h = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i-1-stack[-1]
                max_ = max(max_, last_h*width)
            stack.append(i)
            #print stack
        
        
        return max_
