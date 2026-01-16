# Problem: Swim in Rising Water
# Number: 778
# Difficulty: Hard
# URL: https://leetcode.com/problems/swim-in-rising-water/
# Submission Status: Accepted
# Runtime: 23 ms
# Memory: 19.92 MB

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit.add((0, 0))        visit.add((0, 0))

        while minH:        while minH:
            t, r, c = heapq.heappop(minH)            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:            if r == N - 1 and c == N - 1:
                return t                return t
            for dr, dc in directions:            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR==N or neiC==N or (neiR, neiC) in visit):                if (neiR < 0 or neiC < 0 or neiR==N or neiC==N or (neiR, neiC) in visit):
                    continue                    continue
                visit.add((neiR, neiC))                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
