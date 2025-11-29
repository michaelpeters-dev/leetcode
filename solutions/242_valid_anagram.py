# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        if s_dict==t_dict:
            return True
        else:
            return False
