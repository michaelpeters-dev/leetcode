# Problem: Power of Two
# Number: 231
# Difficulty: Easy
# URL: https://leetcode.com/problems/power-of-two/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 and n&(n-1)==0:
            return True
        else:
            return False
