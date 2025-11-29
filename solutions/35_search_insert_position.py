# Problem: Search Insert Position
# Number: 35
# Difficulty: Easy
# URL: https://leetcode.com/problems/search-insert-position/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1

        while low<=high:
            mid = (low + high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high = mid - 1
            else:
                low = mid + 1
        return low
