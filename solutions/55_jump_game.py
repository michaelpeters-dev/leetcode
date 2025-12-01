# Problem: Jump Game
# Number: 55
# Difficulty: Medium
# URL: https://leetcode.com/problems/jump-game/
# Submission Status: Accepted
# Runtime: 4505 ms
# Memory: 36.51 MB

class Solution:class Solution:
    def canJump(self, nums: List[int]) -> bool:    def canJump(self, nums: List[int]) -> bool:
        memo = {}        memo = {}
        def dfs(i):        def dfs(i):
            if i in memo:            if i in memo:
                return memo[i]                return memo[i]
            if i>=len(nums)-1:            if i>=len(nums)-1:
                return True                return True
                        
            maxJump = nums[i]            maxJump = nums[i]

            for j in range(maxJump, 0, -1):            for j in range(maxJump, 0, -1):
                if dfs(i + j):                if dfs(i + j):
                    memo[i] = True                    memo[i] = True
                    return True                    return True
            memo[i] = False            memo[i] = False
            return False            return False
        return dfs(0)        return dfs(0)
