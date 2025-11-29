# Problem: Find Minimum in Rotated Sorted Array
# Number: 153
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        L = 0
        R = n - 1

        while L<R:
            M = (L+R)//2

            if nums[M]>nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]
