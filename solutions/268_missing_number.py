# Problem: Missing Number
# Number: 268
# Difficulty: Easy
# URL: https://leetcode.com/problems/missing-number/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        n = len(nums)

        # XOR all the indices and numbers together
        for i in range(n):
            xor ^= i^nums[i]

        return xor^n
