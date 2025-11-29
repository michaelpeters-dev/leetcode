# Problem: Reverse Bits
# Number: 190
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-bits/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
