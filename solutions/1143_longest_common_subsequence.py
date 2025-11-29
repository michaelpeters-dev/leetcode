# Problem: Longest Common Subsequence
# Number: 1143
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-common-subsequence/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # O(n * m) Time Complexity
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
