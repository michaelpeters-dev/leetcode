# Problem: Permutations
# Number: 46
# Difficulty: Medium
# URL: https://leetcode.com/problems/permutations/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def permute(self, nums):

        def helper(i, nums):
            if i==len(nums):
                return [[]]

            resPerms = []
            perms = helper(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p[:]
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms

        return helper(0, nums)
