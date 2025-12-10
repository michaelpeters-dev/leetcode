# Problem: Regular Expression Matching
# Number: 10
# Difficulty: Hard
# URL: https://leetcode.com/problems/regular-expression-matching/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            if i >= len(s) and j>=len(p):            if i >= len(s) and j>=len(p):
                return True                return True
            if j >= len(p):            if j >= len(p):
                return False                return False
                        
            match = i < len(s) and (s[i] == p[j] or p[j]==".")            match = i < len(s) and (s[i] == p[j] or p[j]==".")
            if (j + 1) < len(p) and p[j + 1] == "*":            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)]= dfs(i, j + 2) or (match and dfs(i + 1, j))                cache[(i, j)]= dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]                return cache[(i, j)]
                return cache[(i, j)]                return cache[(i, j)]
            if (i, j) in cache:            if (i, j) in cache:

        def dfs(i, j):        def dfs(i, j):
            if match:            if match:
                cache[(i, j)] = dfs(i+1, j+1)                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]                return cache[(i, j)]
            cache[(i, j)] = False            cache[(i, j)] = False
