# Problem: Two Sum II - Input Array Is Sorted
# Number: 167
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submission Status: Accepted
# Runtime: 7 ms
# Memory: 18.59 MB

class Solution:class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1        l, r = 0, len(numbers)-1
        while l<=r:        while l<=r:
            if numbers[l] + numbers[r] == target:            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:            elif numbers[l] + numbers[r] > target:
                r -= 1                r -= 1
            else:            else:
                l += 1                l += 1
        return -1        return -1
