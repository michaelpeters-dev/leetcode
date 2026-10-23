# Problem:    1. Two Sum
# Difficulty: Easy
# Language:   Python3
# Runtime:    1 ms
# Memory:     20.2 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store = {} #Map of the form: number -> index

        index = 0
        for num in nums:
            if target - num in store:
                return [store[target - num], index]
            store[num] = index
            index += 1
