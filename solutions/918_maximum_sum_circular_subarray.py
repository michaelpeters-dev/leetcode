# Problem: Maximum Sum Circular Subarray
# Number: 918
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-sum-circular-subarray/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax
