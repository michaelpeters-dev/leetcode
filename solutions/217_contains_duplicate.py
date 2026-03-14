# Problem: Contains Duplicate
# Number: 217
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Submission Status: Accepted
# Runtime: 19 ms
# Memory: 25.86 MB

class Solution(object):class Solution(object):
    def containsDuplicate(self, nums):    def containsDuplicate(self, nums):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :rtype: bool        :rtype: bool
        """        """
        store = set()        store = set()
        for num in nums:        for num in nums:
            if num in store:            if num in store:
                return True                return True
            store.add(num)            store.add(num)
        return False        return False
                
