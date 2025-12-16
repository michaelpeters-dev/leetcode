# Problem: Jump Game II
# Number: 45
# Difficulty: Medium
# URL: https://leetcode.com/problems/jump-game-ii/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A


        def dfs(i):        def dfs(i):
            #Base Cases            #Base Cases
            if i>=n-1:            if i>=n-1:
                return 0                return 0
            if nums[i]==0:            if nums[i]==0:
                return float('inf')                return float('inf')
            if i in memo:            if i in memo:
                return memo[i]                return memo[i]
                        
            min_jumps = float('inf')            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(i + j))                min_jumps = min(min_jumps, 1 + dfs(i + j))

            memo[i] = min_jumps            memo[i] = min_jumps
            return min_jumps            return min_jumps
        return dfs(0)        return dfs(0)
