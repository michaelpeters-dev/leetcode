# Problem: Subsets
# Number: 78
# Difficulty: Medium
# URL: https://leetcode.com/problems/subsets/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []        res = []
            if i==len(nums):            if i==len(nums):
                copy = visit.copy()                copy = visit.copy()
                res.append(copy)                res.append(copy)
                return                return
                        
            visit.append(nums[i])            visit.append(nums[i])
        def dfs(i, visit):        def dfs(i, visit):
            dfs(i + 1, visit)            dfs(i + 1, visit)
        print(nums[0])        print(nums[0])
            visit.pop()            visit.pop()
            dfs(i + 1, visit)            dfs(i + 1, visit)
                        
        dfs(0, [])        dfs(0, [])
        return res        return res
