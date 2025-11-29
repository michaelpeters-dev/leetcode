# Problem: Coin Change
# Number: 322
# Difficulty: Medium
# URL: https://leetcode.com/problems/coin-change/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for coin in coins:
                if a-coin>=0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount]<float('inf') else -1
