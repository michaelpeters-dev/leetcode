# Problem: Coin Change II
# Number: 518
# Difficulty: Medium
# URL: https://leetcode.com/problems/coin-change-ii/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def change(self, amount: int, coins: List[int]) -> int:    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}        cache = {}
        def dfs(i, a):        def dfs(i, a):
            if a==amount:            if a==amount:
                return 1                return 1
            if a>amount:            if a>amount:
                return 0                return 0
            if i==len(coins):            if i==len(coins):
                return 0                return 0
            if (i, a) in cache:            if (i, a) in cache:
                return cache[(i, a)]                return cache[(i, a)]
                        
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]            return cache[(i, a)]
        return dfs(0, 0)        return dfs(0, 0)
