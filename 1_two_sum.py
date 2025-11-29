# Problem: Two Sum
# Number: 1
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 12.93 MB

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for index, num in enumerate(nums):
            if target-num in dictionary:
                return [dictionary[target-num], index]
            else:
                dictionary[num] = index
   
        
