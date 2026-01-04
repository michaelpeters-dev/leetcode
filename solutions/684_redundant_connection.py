# Problem: Redundant Connection
# Number: 684
# Difficulty: Medium
# URL: https://leetcode.com/problems/redundant-connection/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        def find(n):        def find(n):
        def union(n1, n2):        def union(n1, n2):
            p1, p2 = find(n1), find(n2)            p1, p2 = find(n1), find(n2)
            if p1 == p2:            if p1 == p2:
                return False                return False
            return True            return True

            if n != par[n]:            if n != par[n]:
                par[n] = find(par[n])                par[n] = find(par[n])

            return par[n]            return par[n]
                        
            if rank[p1] > rank[p2]:            if rank[p1] > rank[p2]:
                par[p2] = p1                par[p2] = p1
            else:            else:
                par[p1] = p2                par[p1] = p2
                rank[p1] += rank[p2]                rank[p1] += rank[p2]
                rank[p2] += rank[p1]                rank[p2] += rank[p1]
