# Problem: Decode Ways
# Number: 91
# Difficulty: Medium
# URL: https://leetcode.com/problems/decode-ways/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.88 MB

class Solution:class Solution:
    def numDecodings(self, s: str) -> int:    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1}        dp = { len(s) : 1}

        def dfs(i):        def dfs(i):
            if i in dp:            if i in dp:
                return dp[i]                return dp[i]
            if s[i] == "0":            if s[i] == "0":
                return 0                return 0
                        
            res = dfs(i + 1)            res = dfs(i + 1)
            if ((i + 1) < len(s)) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):            if ((i + 1) < len(s)) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                res += dfs(i + 2)                res += dfs(i + 2)
            return res            return res
            dp[i] = res            dp[i] = res
                
        return dfs(0)        return dfs(0)

