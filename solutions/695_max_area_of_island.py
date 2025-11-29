# Problem: Max Area of Island
# Number: 695
# Difficulty: Medium
# URL: https://leetcode.com/problems/max-area-of-island/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maximum = [0]

        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r, c) in visited or grid[r][c]==0:
                return 0
            visited.add((r, c))
            num = dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            return 1 + num

        for r in range(ROWS):
            for c in range(COLS):
                res = dfs(r, c)
                if res >= maximum[0]:
                    maximum[0] = res
        return maximum[0]
