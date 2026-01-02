# Problem: Valid Parenthesis String
# Number: 678
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-parenthesis-string/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                        
            if s[i]=="(":            if s[i]=="(":
                res = dfs(i + 1, balance + 1)                res = dfs(i + 1, balance + 1)
            if s[i]==")":            if s[i]==")":
                res = dfs(i + 1, balance - 1)                res = dfs(i + 1, balance - 1)
            if s[i]=="*":            if s[i]=="*":
                res =  (                res =  (
                    dfs(i + 1, balance) or                    dfs(i + 1, balance) or
                    dfs(i + 1, balance + 1) or                    dfs(i + 1, balance + 1) or
                    dfs(i + 1, balance - 1)                    dfs(i + 1, balance - 1)
                )                )
        return dfs(0, 0)        return dfs(0, 0)
            memo[(i, balance)] = res            memo[(i, balance)] = res
            return res            return res

