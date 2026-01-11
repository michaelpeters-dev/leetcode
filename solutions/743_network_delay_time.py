# Problem: Network Delay Time
# Number: 743
# Difficulty: Medium
# URL: https://leetcode.com/problems/network-delay-time/
# Submission Status: Accepted
# Runtime: 341 ms
# Memory: 21.17 MB

        t = 0        t = 0

        while minHeap:        while minHeap:
            w1, n1 = heapq.heappop(minHeap)            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:            if n1 in visit:
                continue                continue
            visit.add(n1)            visit.add(n1)
            t = max(t, w1)            t = max(t, w1)
                
            for n2, w2 in edges[n1]:            for n2, w2 in edges[n1]:
                if n2 not in visit:                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2)) #Total path, this is why we add w1 and w2                    heapq.heappush(minHeap, (w1 + w2, n2)) #Total path, this is why we add w1 and w2
                
        return t if len(visit)==n else -1        return t if len(visit)==n else -1
