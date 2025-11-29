# Problem: Sqrt(x)
# Number: 69
# Difficulty: Easy
# URL: https://leetcode.com/problems/sqrtx/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x

        left, right = 1, x//2

        while left<=right:
            mid = (left + right)//2
            if mid*mid == x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        return right
