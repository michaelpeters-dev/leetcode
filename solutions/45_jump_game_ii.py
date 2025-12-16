# Problem: Jump Game II
# Number: 45
# Difficulty: Medium
# URL: https://leetcode.com/problems/jump-game-ii/
# Submission Status: Accepted
# Runtime: 12 ms
# Memory: 18.44 MB

class Solution:class Solution:
    def jump(self, nums: List[int]) -> int:    def jump(self, nums: List[int]) -> int:
        res = 0        res = 0
        l, r = 0, 0        l, r = 0, 0
                
        while r < len(nums) - 1:        while r < len(nums) - 1:
            farthest = 0            farthest = 0
            for i in range(l, r + 1):            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])                farthest = max(farthest, i + nums[i])
            l = r + 1            l = r + 1
            r = farthest            r = farthest
            res += 1            res += 1
        return res        return res
