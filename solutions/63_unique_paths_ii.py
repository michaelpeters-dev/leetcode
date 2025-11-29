# Problem: Unique Paths II
# Number: 63
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-paths-ii/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N-1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
                else:
                    dp[c] = dp[c] + 0
        return dp[0]
