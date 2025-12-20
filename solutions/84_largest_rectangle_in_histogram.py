# Problem: Largest Rectangle in Histogram
# Number: 84
# Difficulty: Hard
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0        maxArea = 0
        stack = [] # Hold a pair: (index, height)        stack = [] # Hold a pair: (index, height)
                
        for i, h in enumerate(heights):        for i, h in enumerate(heights):
            start = i            start = i
            while stack and stack[-1][1] > h:            while stack and stack[-1][1] > h:
                index, height = stack.pop()                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))                maxArea = max(maxArea, height * (i - index))
                start = index                start = index
            stack.append((start, h))            stack.append((start, h))
                
        for i, h in stack:        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea        return maxArea
