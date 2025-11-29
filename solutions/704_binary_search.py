# Problem: Binary Search
# Number: 704
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-search/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def search(self, nums, target):
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l + r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
