# Problem: Plus One
# Number: 66
# Difficulty: Easy
# URL: https://leetcode.com/problems/plus-one/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def plusOne(self, digits):
        digits[-1] = digits[-1] + 1

        for r in range(len(digits)-1, 0,-1):
            if digits[r]==10:
                digits[r] = 0
                digits[r - 1] = digits[r - 1] + 1

        if digits[0]==10:
            digits = [1, 0] + digits[1:]

        return digits
