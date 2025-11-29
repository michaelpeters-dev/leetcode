# Problem: Contains Duplicate II
# Number: 219
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate-ii/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        encountered = {}

        for index, num in enumerate(nums):
            if num not in encountered:
                encountered[num] = index
            else:
                if abs(index-encountered[num])<=k:
                    return True
                else:
                    encountered[num] = index
        return False
