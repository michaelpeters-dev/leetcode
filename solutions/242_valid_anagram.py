# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution(object):class Solution(object):
    def isAnagram(self, s, t):    def isAnagram(self, s, t):
        """        """
        :type s: str        :type s: str
        :type t: str        :type t: str
        :rtype: bool        :rtype: bool
        """        """
        if len(s) != len(t):        if len(s) != len(t):
            return False            return False

        first = defaultdict(int)        first = defaultdict(int)
        second = defaultdict(int)        second = defaultdict(int)

        for i in range(0, len(s)):        for i in range(0, len(s)):
            first[s[i]] += 1            first[s[i]] += 1
                
        return first == second        return first == second
            second[t[i]] += 1            second[t[i]] += 1
                
