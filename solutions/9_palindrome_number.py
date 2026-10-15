# Problem:    9. Palindrome Number
# Difficulty: Easy
# Language:   Python3
# Runtime:    9 ms
# Memory:     19.2 MB
# Solved:     2026-10-15
# URL:        https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        strX = str(x)
        l = 0
        r  = len(strX) - 1

        while (l <= r):
            if (strX[l] != strX[r]):
                return False
            l += 1
            r -= 1
        return True
