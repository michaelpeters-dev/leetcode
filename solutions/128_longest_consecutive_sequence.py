# Problem: Longest Consecutive Sequence
# Number: 128
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution(object):class Solution(object):
    def longestConsecutive(self, nums):    def longestConsecutive(self, nums):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :rtype: int        :rtype: int
        """        """

        # Add them all to a set        # Add them all to a set
        # Then iterate through, if we don't have a number - 1 in the set then that's where we count from        # Then iterate through, if we don't have a number - 1 in the set then that's where we count from

        store = set()        store = set()
        for num in nums:        for num in nums:
            store.add(num)            store.add(num)

        for num in store:        for num in store:
        longest = 0        longest = 0
            if (num - 1) not in store:            if (num - 1) not in store:
                counter = 1                counter = 1
                while (num + 1) in store:                while (num + 1) in store:
                    counter += 1                    counter += 1
                    num += 1                    num += 1
                longest = max(longest, counter)                longest = max(longest, counter)
            else:            else:
                continue                continue
        return longest        return longest
