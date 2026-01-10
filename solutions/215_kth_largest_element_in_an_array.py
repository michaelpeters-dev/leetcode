# Problem: Kth Largest Element in an Array
# Number: 215
# Difficulty: Medium
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submission Status: Accepted
# Runtime: 61 ms
# Memory: 38.73 MB

class Solution:class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:    def findKthLargest(self, nums: List[int], k: int) -> int:
    # quickselect solution    # quickselect solution
        k = len(nums) - k # use k as an index instead        k = len(nums) - k # use k as an index instead

        def quickSelect(l, r):        def quickSelect(l, r):
            mid = (l + r) // 2            mid = (l + r) // 2
            nums[mid], nums[r] = nums[r], nums[mid]            nums[mid], nums[r] = nums[r], nums[mid]
            pivot, p = nums[r], l            pivot, p = nums[r], l
            for i in range(l, r):            for i in range(l, r):
                if nums[i] <= pivot:                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1                    p += 1
            nums[p], nums[r] = nums[r], nums[p]            nums[p], nums[r] = nums[r], nums[p]

            if k < p: return quickSelect(l, p - 1)            if k < p: return quickSelect(l, p - 1)
            elif k > p: return quickSelect(p + 1, r)            elif k > p: return quickSelect(p + 1, r)
            else: return nums[p]            else: return nums[p]
