# Problem: Valid Palindrome
# Number: 125
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-palindrome/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        L = 0
        R = n - 1
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"
        while L<R:
            print(s[L], s[R])
            if s[L].lower() not in letters:
                L += 1
                continue
            elif s[R].lower() not in letters:
                R -= 1
                continue

            if s[L].lower()!=s[R].lower():
                return False
            L += 1
            R -= 1
        return True
