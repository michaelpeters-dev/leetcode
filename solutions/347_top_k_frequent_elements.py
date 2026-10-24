# Problem:    347. Top K Frequent Elements
# Difficulty: Medium
# Language:   Python3
# Runtime:    15 ms
# Memory:     24.8 MB
# Solved:     2026-10-23
# URL:        https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int) #This stores the item then the count of it

        for num in nums:
            count[num] += 1

        store = [[] for i in range(len(nums))] #1[...] 2[..]
        for number, amount in count.items():
            store[amount - 1].append(number)
        
        result = []
        for i in range(len(store) - 1, -1, -1):
            for j in range(len(store[i])):
                if (k == 0):
                    return result
                k -= 1
                result.append(store[i][j])
        return result
