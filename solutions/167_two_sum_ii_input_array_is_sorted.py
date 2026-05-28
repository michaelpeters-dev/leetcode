# Problem: Two Sum II - Input Array Is Sorted
# Number: 167
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution(object):class Solution(object):
    def twoSum(self, numbers, target):    def twoSum(self, numbers, target):
        """        """
        :type numbers: List[int]        :type numbers: List[int]
        :type target: int        :type target: int
        :rtype: List[int]        :rtype: List[int]
        """        """
        r = len(numbers) - 1        r = len(numbers) - 1
            if (total == target):            if (total == target):

                return [l, r]                return [l, r]
        while l<r:        while l<r:
            total = numbers[l] + numbers[r]            total = numbers[l] + numbers[r]
            elif (total < target):            elif (total < target):
                l += 1                l += 1
            else:            else:
        l = 0        l = 0
                r -= 1                r -= 1
