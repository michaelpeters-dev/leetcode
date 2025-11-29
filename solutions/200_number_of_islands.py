# Problem: Number of Islands
# Number: 200
# Difficulty: Medium
# URL: https://leetcode.com/problems/number-of-islands/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        counter = [0]
        visited = set()

        def dfs(r, c, visited):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r, c) in visited or grid[r][c]=="0":
                return False
            visited.add((r, c))
            dfs(r - 1, c,visited)
            dfs(r + 1, c,visited)
            dfs(r, c - 1,visited)
            dfs(r, c + 1,visited)
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c,visited):
                    counter[0] += 1
        return counter[0]
