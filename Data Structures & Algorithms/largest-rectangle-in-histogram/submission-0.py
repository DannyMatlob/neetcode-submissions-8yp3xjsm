class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # where each element represents (height, index)
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                curH, curI = stack.pop()
                maxArea = max(maxArea, curH * (i - curI))
                start = curI
            
            stack.append((height, start))
        
        for h, i in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
            


        