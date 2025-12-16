# Problem: Jump Game II
# Number: 45
# Difficulty: Medium
# URL: https://leetcode.com/problems/jump-game-ii/
# Submission Status: Accepted
# Runtime: 5222 ms
# Memory: 18.59 MB

class Solution:class Solution:
    def jump(self, nums: List[int]) -> int:    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * (len(nums))        dp = [float('inf')] * (len(nums))
        for i in range(len(nums)-2, -1, -1):        for i in range(len(nums)-2, -1, -1):
                if i + j < len(nums):                if i + j < len(nums):

            for j in range(1, nums[i] + 1):            for j in range(1, nums[i] + 1):
        return dp[0]        return dp[0]
        dp[len(nums)-1] = 0        dp[len(nums)-1] = 0

                    dp[i] = min(dp[i], 1 + dp[i + j])                    dp[i] = min(dp[i], 1 + dp[i + j])

