# Problem: Coin Change II
# Number: 518
# Difficulty: Medium
# URL: https://leetcode.com/problems/coin-change-ii/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def change(self, amount: int, coins: List[int]) -> int:    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)        dp[0] = [1] * (len(coins) + 1)

        for a in range(1, amount + 1):        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]        return dp[amount][0]
