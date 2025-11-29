# Problem: Range Sum Query - Immutable
# Number: 303
# Difficulty: Easy
# URL: https://leetcode.com/problems/range-sum-query-immutable/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left, right):
       rightSum = self.prefix[right]
       leftSum = self.prefix[left - 1] if left>0 else 0
       return rightSum - leftSum
