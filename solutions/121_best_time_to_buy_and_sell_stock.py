# Problem: Best Time to Buy and Sell Stock
# Number: 121
# Difficulty: Easy
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L, R = 0, 1
        max_profit = 0
        for R in range(1, len(prices)):
            #profitable?
            if prices[R]-prices[L]>0:
                profit = prices[R]-prices[L]
                max_profit = max(max_profit, profit)
            if prices[R]<prices[L]:
                L = R
        return max_profit
