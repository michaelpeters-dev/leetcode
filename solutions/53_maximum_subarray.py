# Problem: Maximum Subarray
# Number: 53
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-subarray/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        max_sub = nums[0]
        for num in nums:
            if cur_sum<0:
                cur_sum = 0
            cur_sum += num
            max_sub = max(max_sub, cur_sum)
        return max_sub
