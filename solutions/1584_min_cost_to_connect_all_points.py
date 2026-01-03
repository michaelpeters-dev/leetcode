# Problem: Min Cost to Connect All Points
# Number: 1584
# Difficulty: Medium
# URL: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Submission Status: Accepted
# Runtime: 2616 ms
# Memory: 177.36 MB

class Solution:class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)        N = len(points)

        adj = { i:[] for i in range(N) } # i : : list of [cost, node]        adj = { i:[] for i in range(N) } # i : : list of [cost, node]

        for i in range(N):        for i in range(N):
            x1, y1 = points[i]            x1, y1 = points[i]
            for j in range(i + 1, N):            for j in range(i + 1, N):
                x2, y2 = points[j]                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])                adj[i].append([dist, j])
                adj[j].append([dist, i])                adj[j].append([dist, i])
                
        # Prim's algorithm        # Prim's algorithm
        res = 0        res = 0
        visit = set()        visit = set()
