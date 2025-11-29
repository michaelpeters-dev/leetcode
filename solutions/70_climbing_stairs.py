# Problem: Climbing Stairs
# Number: 70
# Difficulty: Easy
# URL: https://leetcode.com/problems/climbing-stairs/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def climbStairs(self, n: int) -> int:
        trace = [0, 1]
        for i in range(1, n+1):
            total = sum(trace)
            trace[0] = trace[1]
            trace[1] = total
        return trace[1]
