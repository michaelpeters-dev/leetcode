# Problem: Min Cost Climbing Stairs
# Number: 746
# Difficulty: Easy
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}        memo = {}
        def dfs(i):        def dfs(i):
            if i>=len(cost):            if i>=len(cost):
                return 0                return 0
            minimum = cost[i] + min(dfs(i + 1), dfs(i + 2))            minimum = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]            return memo[i]
        res = min(dfs(0), dfs(1))        res = min(dfs(0), dfs(1))
            if i in memo:            if i in memo:
                return memo[i]                return memo[i]
            memo[i] = minimum            memo[i] = minimum
        return res        return res
