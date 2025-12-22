# Problem: Single Number
# Number: 136
# Difficulty: Easy
# URL: https://leetcode.com/problems/single-number/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def singleNumber(self, nums: List[int]) -> int:    def singleNumber(self, nums: List[int]) -> int:
        i = 0        i = 0
        nums.sort()        nums.sort()
        while i<len(nums):        while i<len(nums):
            if i==len(nums)-1 or nums[i]!=nums[i+1]:            if i==len(nums)-1 or nums[i]!=nums[i+1]:
                return nums[i]                return nums[i]
            else:            else:
                i = i + 2                i = i + 2
