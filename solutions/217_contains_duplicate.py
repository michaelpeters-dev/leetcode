# Problem:    217. Contains Duplicate
# Difficulty: Easy
# Language:   Python3
# Runtime:    18 ms
# Memory:     32.4 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        store = set()
        for num in nums:
            if num in store:
                return True
            store.add(num)
        return False
