# Problem: Search in Rotated Sorted Array
# Number: 33
# Difficulty: Medium
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target==nums[mid]:
                return mid

            if nums[mid]>=nums[l]:
                if target>nums[mid]:
                    l = mid + 1
                elif target<nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target>nums[r]:
                    r = mid - 1
                elif target<nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
