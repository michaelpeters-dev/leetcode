# Problem: First Bad Version
# Number: 278
# Difficulty: Easy
# URL: https://leetcode.com/problems/first-bad-version/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def firstBadVersion(self, n):
        def helper(l, r):
            if l > r:
                return l
            m = l + (r - l) // 2
            if isBadVersion(m):
                return helper(l, m - 1)
            else:
                return helper(m + 1, r)

        return helper(1, n)
