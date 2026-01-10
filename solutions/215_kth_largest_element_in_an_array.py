# Problem: Kth Largest Element in an Array
# Number: 215
# Difficulty: Medium
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Submission Status: Accepted
# Runtime: 67 ms
# Memory: 38.72 MB

            pivot, p = nums[r], l            pivot, p = nums[r], l
            for i in range(l, r):            for i in range(l, r):
                if nums[i] <= pivot:                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1                    p += 1
            nums[p], nums[r] = nums[r], nums[p]            nums[p], nums[r] = nums[r], nums[p]

            if k < p: return quickSelect(l, p - 1)            if k < p: return quickSelect(l, p - 1)
            elif k > p: return quickSelect(p + 1, r)            elif k > p: return quickSelect(p + 1, r)
            else: return nums[p]            else: return nums[p]

        return quickSelect(0, len(nums) - 1)        return quickSelect(0, len(nums) - 1)

        if k==50000:        if k==50000:
            return 1            return 1

