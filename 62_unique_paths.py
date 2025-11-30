# Problem: Unique Paths
# Number: 62
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-paths/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.90 MB

class Solution:class Solution:
    def uniquePaths(self, m: int, n: int) -> int:    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * (n + 1)] * (m + 1)        res = [[0] * (n + 1)] * (m + 1)
        res[m-1][n-1] = 1        res[m-1][n-1] = 1

        for r in range(m-1, -1, -1):        for r in range(m-1, -1, -1):
            for c in range(n - 1, -1, -1):            for c in range(n - 1, -1, -1):
                res[r][c] = res[r + 1][c] + res[r][c + 1]                res[r][c] = res[r + 1][c] + res[r][c + 1]
                
        return res[0][0]        return res[0][0]

