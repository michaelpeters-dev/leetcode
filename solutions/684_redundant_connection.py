# Problem: Redundant Connection
# Number: 684
# Difficulty: Medium
# URL: https://leetcode.com/problems/redundant-connection/
# Submission Status: Accepted
# Runtime: 36 ms
# Memory: 17.80 MB

class Solution:class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)        N = len(edges)
        par = [i for i in range(N + 1)] #ith node ->. parent (1 - n)        par = [i for i in range(N + 1)] #ith node ->. parent (1 - n)
        rank = [1] * (N + 1)        rank = [1] * (N + 1)

        def find(n):        def find(n):
            if n != par[n]:            if n != par[n]:
                par[n] = find(par[n])                par[n] = find(par[n])
            return par[n]            return par[n]

        def union(n1, n2):        def union(n1, n2):
            p1, p2 = find(n1), find(n2)            p1, p2 = find(n1), find(n2)
            if p1 == p2:            if p1 == p2:
                return False                return False
                        
            if rank[p1] > rank[p2]:            if rank[p1] > rank[p2]:
