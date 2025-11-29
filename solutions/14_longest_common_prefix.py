# Problem: Longest Common Prefix
# Number: 14
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-common-prefix/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            while not s.startswith(res):
                res = res[:-1]
            if not res:
                return ""
        return res
