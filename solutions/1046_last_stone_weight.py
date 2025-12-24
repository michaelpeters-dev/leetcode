# Problem: Last Stone Weight
# Number: 1046
# Difficulty: Easy
# URL: https://leetcode.com/problems/last-stone-weight/
# Submission Status: Accepted
# Runtime: 1 ms
# Memory: 17.42 MB

class Solution:class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]        stones = [-s for s in stones]
        heapq.heapify(stones)        heapq.heapify(stones)

        while len(stones) > 1:        while len(stones) > 1:
            first = heapq.heappop(stones)            first = heapq.heappop(stones)
            second = heapq.heappop(stones)            second = heapq.heappop(stones)
            if second > first:            if second > first:
                heapq.heappush(stones, first - second)                heapq.heappush(stones, first - second)
        return abs(stones[0])        return abs(stones[0])
        stones.append(0)        stones.append(0)
                
