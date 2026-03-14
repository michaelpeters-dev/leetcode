# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 7 ms
# Memory: 14.18 MB

from collections import defaultdictfrom collections import defaultdict
    def isAnagram(self, s, t):    def isAnagram(self, s, t):
        """        """
        :type s: str        :type s: str
        :type t: str        :type t: str
        :rtype: bool        :rtype: bool
        """        """
        set_a = defaultdict(int)        set_a = defaultdict(int)
        set_b = defaultdict(int)        set_b = defaultdict(int)
        if len(s) != len(t):        if len(s) != len(t):
            return False            return False
                
        for i in range(0, len(s)):        for i in range(0, len(s)):
class Solution(object):class Solution(object):
            set_a[s[i]] += 1            set_a[s[i]] += 1
            set_b[t[i]] += 1            set_b[t[i]] += 1
                
        return set_a == set_b        return set_a == set_b
