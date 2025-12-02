# Problem: Find the Index of the First Occurrence in a String
# Number: 28
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.52 MB

class Solution:class Solution:
    def strStr(self, haystack: str, needle: str) -> int:    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle) + 1):        for i in range(0, len(haystack)-len(needle) + 1):
            temp = haystack[i: i + len(needle)]            temp = haystack[i: i + len(needle)]
            if temp==needle:            if temp==needle:
                return i                return i
        return -1        return -1
            print(temp)            print(temp)
                
