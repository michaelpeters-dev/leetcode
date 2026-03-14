# Problem: Product of Array Except Self
# Number: 238
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submission Status: Accepted
# Runtime: 32 ms
# Memory: 20.19 MB

class Solution(object):class Solution(object):
    def productExceptSelf(self, nums):    def productExceptSelf(self, nums):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :rtype: List[int]        :rtype: List[int]
        """        """
        n = len(nums)        n = len(nums)
        result = [1] * n        result = [1] * n

        prefix = 1        prefix = 1
        for i in range(n):        for i in range(n):
            result[i] = prefix            result[i] = prefix
            prefix *= nums[i]            prefix *= nums[i]
                
        suffix = 1        suffix = 1
        for i in range(n-1, -1, -1):        for i in range(n-1, -1, -1):
            result[i] *= suffix            result[i] *= suffix
            suffix *= nums[i]            suffix *= nums[i]
        return result        return result
                
