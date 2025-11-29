# Problem: House Robber II
# Number: 213
# Difficulty: Medium
# URL: https://leetcode.com/problems/house-robber-ii/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(numbers):
            rob1, rob2 = 0, 0

            for n in numbers:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])
