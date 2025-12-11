# Problem: Rotting Oranges
# Number: 994
# Difficulty: Medium
# URL: https://leetcode.com/problems/rotting-oranges/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            for i in range(len(q)):            for i in range(len(q)):
                r, c = q.popleft()                r, c = q.popleft()
                for dr, dc in directions:                for dr, dc in directions:
                    row, col = dr + r, dc + c                    row, col = dr + r, dc + c
                    # Check out of bounds, and if it can even be made rotten                    # Check out of bounds, and if it can even be made rotten
                    if (row<0 or col<0) or (row==ROWS or col==COLS) or (grid[row][col] != 1):                    if (row<0 or col<0) or (row==ROWS or col==COLS) or (grid[row][col] != 1):
                        continue                        continue
                    grid[row][col] = 2                    grid[row][col] = 2
                    q.append([row, col])                    q.append([row, col])
                    fresh -= 1                    fresh -= 1
            time += 1            time += 1
        return time if fresh==0 else - 1        return time if fresh==0 else - 1

        while q and fresh > 0:        while q and fresh > 0:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
