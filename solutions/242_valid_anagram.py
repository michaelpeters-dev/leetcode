# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 11 ms
# Memory: 12.41 MB

class Solution(object):class Solution(object):
    def isAnagram(self, s, t):    def isAnagram(self, s, t):
        """        """
        :type s: str        :type s: str
        :type t: str        :type t: str
        :rtype: bool        :rtype: bool
        """        """
        first = defaultdict(int)        first = defaultdict(int)
        second = defaultdict(int)        second = defaultdict(int)

        for letter in s:        for letter in s:
            first[letter] += 1            first[letter] += 1
                
        for letter in t:        for letter in t:
            second[letter] += 1            second[letter] += 1

        return first == second        return first == second
