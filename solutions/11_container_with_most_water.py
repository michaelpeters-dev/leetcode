# Problem: Container With Most Water
# Number: 11
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0

        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
