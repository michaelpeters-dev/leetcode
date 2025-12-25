# Problem: Distinct Subsequences
# Number: 115
# Difficulty: Hard
# URL: https://leetcode.com/problems/distinct-subsequences/
# Submission Status: Accepted
# Runtime: 224 ms
# Memory: 17.26 MB

class Solution:class Solution:
    def numDistinct(self, s: str, t: str) -> int:    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)        ROWS, COLS = len(s), len(t)

        dp = [0] * (COLS + 1)        dp = [0] * (COLS + 1)
        dp[COLS] = 1        dp[COLS] = 1

        for r in range(ROWS - 1, -1, -1):        for r in range(ROWS - 1, -1, -1):
            prev_diag = 1 # grid[r+1][COLS] in 2D solution            prev_diag = 1 # grid[r+1][COLS] in 2D solution
                        
            for c in range(COLS - 1, -1, -1):            for c in range(COLS - 1, -1, -1):
                temp = dp[c] # save grid[r + 1][c]                temp = dp[c] # save grid[r + 1][c]
                if s[r]==t[c]:                if s[r]==t[c]:
                    dp[c] += prev_diag                    dp[c] += prev_diag
                prev_diag = temp                prev_diag = temp
        return dp[0]        return dp[0]
