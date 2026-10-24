# Problem:    128. Longest Consecutive Sequence
# Difficulty: Medium
# Language:   Python3
# Runtime:    50 ms
# Memory:     36.5 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        store = set()
        for num in nums:
            store.add(num)
        
        result = 0

        for num in store:
            if (num - 1 in store):
                continue

            tempCount = 0
            while(num in store):
                tempCount += 1
                num += 1

            result = max(result, tempCount)
        
        return result
