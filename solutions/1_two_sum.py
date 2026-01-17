# Problem: Two Sum
# Number: 1
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 13.16 MB

class Solution(object):class Solution(object):
    def twoSum(self, nums, target):    def twoSum(self, nums, target):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :type target: int        :type target: int
        :rtype: List[int]        :rtype: List[int]
        """        """
        dictionary = {}        dictionary = {}
        for index, num in enumerate(nums):        for index, num in enumerate(nums):
            if target-num in dictionary:            if target-num in dictionary:
                return [dictionary[target-num], index]                return [dictionary[target-num], index]
            else:            else:
                dictionary[num] = index                dictionary[num] = index
      
