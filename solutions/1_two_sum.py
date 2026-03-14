# Problem: Two Sum
# Number: 1
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 12.96 MB

class Solution(object):class Solution(object):
    def twoSum(self, nums, target):    def twoSum(self, nums, target):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :type target: int        :type target: int
        :rtype: List[int]        :rtype: List[int]
        """        """
        store = {}        store = {}

        for index, num in enumerate(nums):        for index, num in enumerate(nums):
            if target - num in store:            if target - num in store:
                return [store[target - num], index]                return [store[target - num], index]
            else:            else:
                store[num] = index                store[num] = index
