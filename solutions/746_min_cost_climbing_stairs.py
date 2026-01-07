# Problem: Min Cost Climbing Stairs
# Number: 746
# Difficulty: Easy
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/
# Submission Status: Accepted
# Runtime: 4 ms
# Memory: 19.44 MB

class Solution:class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)        dp = [0] * (len(cost) + 2)
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])        return min(dp[0], dp[1])
        for i in range(len(cost) - 1, -1, -1):        for i in range(len(cost) - 1, -1, -1):

