# Problem: House Robber
# Number: 198
# Difficulty: Medium
# URL: https://leetcode.com/problems/house-robber/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
