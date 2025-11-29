# Problem: Palindromic Substrings
# Number: 647
# Difficulty: Medium
# URL: https://leetcode.com/problems/palindromic-substrings/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    longest += 1
                else:
                    break
                l -= 1
                r += 1

            l, r = i, i+1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    longest += 1
                else:
                    break
                l -= 1
                r += 1
        return longest
