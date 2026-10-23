# Problem:    242. Valid Anagram
# Difficulty: Easy
# Language:   Python3
# Runtime:    9 ms
# Memory:     19.3 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for letter in s:
            sMap[letter] += 1

        for letter in t:
            tMap[letter] += 1
        
        return sMap == tMap
