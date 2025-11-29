# Problem: Longest Consecutive Sequence
# Number: 128
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n-1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                    longest = max(longest, length)
        return longest
