# Problem: Unique Paths
# Number: 62
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-paths/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def uniquePaths(self, m, n):
        prevRow = [0] * n

        for r in range(m-1, -1, -1):
            curRow = [0] * n
            curRow[n - 1] = 1
            for c in range(n - 2, -1, -1):
                curRow[c]=curRow[c+1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]
