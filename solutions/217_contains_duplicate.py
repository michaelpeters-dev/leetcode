# Problem: Contains Duplicate
# Number: 217
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Submission Status: Accepted
# Runtime: 24 ms
# Memory: 26.00 MB

class Solution(object):class Solution(object):
    def containsDuplicate(self, nums):    def containsDuplicate(self, nums):
        """        """
        :type nums: List[int]        :type nums: List[int]
        :rtype: bool        :rtype: bool
        """        """
        store = set()        store = set()

        for num in nums:        for num in nums:
            if num not in store:            if num not in store:
                store.add(num)                store.add(num)
            else:            else:
                return True                return True
        return False        return False
                
