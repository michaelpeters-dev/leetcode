# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 11 ms
# Memory: 14.35 MB

from collections import defaultdictfrom collections import defaultdict
class Solution(object):class Solution(object):
    def isAnagram(self, s, t):    def isAnagram(self, s, t):
        """        """
        :type s: str        :type s: str
        :type t: str        :type t: str
        :rtype: bool        :rtype: bool
        """        """
        if len(s) != len(t):        if len(s) != len(t):
            return False            return False

        set_a = defaultdict(int)        set_a = defaultdict(int)
        set_b = defaultdict(int)        set_b = defaultdict(int)

        for i in range(len(s)):        for i in range(len(s)):

            set_a[s[i]] += 1            set_a[s[i]] += 1
            set_b[t[i]] += 1            set_b[t[i]] += 1

        return set_a == set_b        return set_a == set_b
                
