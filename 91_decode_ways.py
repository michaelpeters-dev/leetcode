# Problem: Decode Ways
# Number: 91
# Difficulty: Medium
# URL: https://leetcode.com/problems/decode-ways/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 18.32 MB

        def dfs(i):        def dfs(i):
                        
            if i>=len(s):            if i>=len(s):
                return 1                return 1
            else:            else:
            if (i+1)<=len(s)-1 and s[i:i+2] in mappings:            if (i+1)<=len(s)-1 and s[i:i+2] in mappings:
            if s[i]=="0":            if s[i]=="0":
                return 0                return 0
            if i in dp:            if i in dp:
                return dp[i]                return dp[i]

                return value                return value
                value = dfs(i + 1) + dfs(i + 2)                value = dfs(i + 1) + dfs(i + 2)
                dp[i] = value                dp[i] = value
                return value                return value
                value = dfs(i + 1)                value = dfs(i + 1)
                dp[i] = value                dp[i] = value
                
        return dfs(0)        return dfs(0)
