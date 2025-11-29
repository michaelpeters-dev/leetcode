# Problem: Longest Repeating Character Replacement
# Number: 424
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-repeating-character-replacement/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            while (r-l+1)-(max(count.values())) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res
