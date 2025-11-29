# Problem: Palindrome Number
# Number: 9
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome-number/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
