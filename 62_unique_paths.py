# Problem: Unique Paths
# Number: 62
# Difficulty: Medium
# URL: https://leetcode.com/problems/unique-paths/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        def dfs(r, c):        def dfs(r, c):
            if r>=m or c>=n:            if r>=m or c>=n:
                return 0                return 0

            count = dfs(r + 1, c) + dfs(r, c + 1)            count = dfs(r + 1, c) + dfs(r, c + 1)

            return count            return count
                
        return dfs(0, 0)        return dfs(0, 0)
            if r==ENDPOINT[0] and c==ENDPOINT[1]:            if r==ENDPOINT[0] and c==ENDPOINT[1]:
                return 1                return 1
            dp[(r, c)] = count            dp[(r, c)] = count
            if (r, c) in dp:            if (r, c) in dp:
                return dp[(r, c)]                return dp[(r, c)]
        
