# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution(object):class Solution(object):
    def topKFrequent(self, nums, k):    def topKFrequent(self, nums, k):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :type k: int        :type k: int
        :rtype: List[int]        :rtype: List[int]
        """        """
        store = {}        store = {}
        for num in nums:        for num in nums:
            if num not in store:            if num not in store:
                store[num] = 1                store[num] = 1
            else:            else:
                store[num] += 1                store[num] += 1
                
        sorted_nums = sorted(store, key=store.get, reverse=True)        sorted_nums = sorted(store, key=store.get, reverse=True)

        return sorted_nums[:k]        return sorted_nums[:k]
