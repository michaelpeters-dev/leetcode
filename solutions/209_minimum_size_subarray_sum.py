# Problem: Minimum Size Subarray Sum
# Number: 209
# Difficulty: Medium
# URL: https://leetcode.com/problems/minimum-size-subarray-sum/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def minSubArrayLen(self, target, nums):
        L, total = 0, 0
        length = float("inf")

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1
        return 0 if length == float("inf") else length
