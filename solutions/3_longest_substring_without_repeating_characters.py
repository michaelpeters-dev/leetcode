# Problem: Longest Substring Without Repeating Characters
# Number: 3
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, r-l+1)
        return res
