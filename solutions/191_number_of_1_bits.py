# Problem: Number of 1 Bits
# Number: 191
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-1-bits/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n!=0:
            n = n & (n-1)
            ans += 1
        return ans
