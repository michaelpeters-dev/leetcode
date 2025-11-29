# Problem: Maximum Product Subarray
# Number: 152
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-product-subarray/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        cur_max = 1
        cur_min = 1

        for num in nums:
            if num == 0:
                cur_max = 1
                cur_min = 1
                continue
            tmp = cur_max * num
            cur_max = max(num * cur_max, num*cur_min, num)
            cur_min = min(tmp, num * cur_min, num)
            res = max(res, cur_max)
        return res
