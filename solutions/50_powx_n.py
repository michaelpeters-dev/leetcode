# Problem: Pow(x, n)
# Number: 50
# Difficulty: Medium
# URL: https://leetcode.com/problems/powx-n/
# Submission Status: Accepted
# Runtime: 2 ms
# Memory: N/A

class Solution:class Solution:
    def myPow(self, x: float, n: int) -> float:    def myPow(self, x: float, n: int) -> float:
            def helper(x, n):            def helper(x, n):
                if x==0:                if x==0:
                    return 0                    return 0
                if n==0:                if n==0:
                    return 1                    return 1

            res = helper(x, abs(n))            res = helper(x, abs(n))
                                
                res = helper(x, n//2)                res = helper(x, n//2)

                res = res * res                res = res * res
                return x * res if n%2!=0 else res                return x * res if n%2!=0 else res
            return res if n>=0 else 1/res            return res if n>=0 else 1/res
