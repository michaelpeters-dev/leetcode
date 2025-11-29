# Problem: Remove Element
# Number: 27
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-element/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        for r in range(0, len(nums)):
            if nums[r]!=val:
                nums[l] = nums[r]
                l += 1
        return l
