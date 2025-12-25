# Problem: Distinct Subsequences
# Number: 115
# Difficulty: Hard
# URL: https://leetcode.com/problems/distinct-subsequences/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def numDistinct(self, s: str, t: str) -> int:    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)        ROWS, COLS = len(s), len(t)
        grid = [[0] * (COLS + 1) for _ in range(ROWS + 1)]        grid = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS - 1, -1, -1):        for r in range(ROWS - 1, -1, -1):
                    grid[r][c] = grid[r+1][c] + grid[r + 1][c + 1]                    grid[r][c] = grid[r+1][c] + grid[r + 1][c + 1]
                else:                else:
                    grid[r][c] = grid[r + 1][c]                    grid[r][c] = grid[r + 1][c]
            for c in range(COLS - 1, -1, -1):            for c in range(COLS - 1, -1, -1):
        grid[ROWS][COLS] = 1        grid[ROWS][COLS] = 1
                if s[r]==t[c]:                if s[r]==t[c]:
        for r in range(ROWS + 1 ):        for r in range(ROWS + 1 ):
            grid[r][COLS] = 1            grid[r][COLS] = 1

        return grid[0][0]        return grid[0][0]
