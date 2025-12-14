# Problem: Combination Sum II
# Number: 40
# Difficulty: Medium
# URL: https://leetcode.com/problems/combination-sum-ii/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []        res = []
        candidates.sort()        candidates.sort()

        def dfs(i, cur, total):        def dfs(i, cur, total):
            if total==target:            if total==target:
                res.append(cur.copy())                res.append(cur.copy())
                return                return
            if total > target or i == len(candidates):            if total > target or i == len(candidates):
                return                return
           ·‌           ·‌
            # Include a candidate            # Include a candidate
            cur.append(candidates[i])            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])            dfs(i + 1, cur, total + candidates[i])
            cur.pop()            cur.pop()

            # Skip a candidate            # Skip a candidate
