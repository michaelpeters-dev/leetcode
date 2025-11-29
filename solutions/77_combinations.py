# Problem: Combinations
# Number: 77
# Difficulty: Medium
# URL: https://leetcode.com/problems/combinations/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def combine(self, n, k):
        combs = []

        def helper(i, curComb, n, k):
            if len(curComb) == k:
                combs.append(curComb[:])
                return
            if i > n:
                return
            for j in range(i, n + 1):
                curComb.append(j)
                helper(j + 1, curComb, n, k)
                curComb.pop()

        helper(1, [], n, k)
        return combs
