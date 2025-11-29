# Problem: Length of Last Word
# Number: 58
# Difficulty: Easy
# URL: https://leetcode.com/problems/length-of-last-word/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])
