# Problem: Rotting Oranges
# Number: 994
# Difficulty: Medium
# URL: https://leetcode.com/problems/rotting-oranges/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A


        print(queue)        print(queue)
        print(fresh)        print(fresh)

        combinations = [[1, 0], [-1, 0], [0, -1], [0, 1]]        combinations = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        while queue and fresh>0:        while queue and fresh>0:
            snap_shot = len(queue)            snap_shot = len(queue)
            for _ in range(snap_shot):            for _ in range(snap_shot):
                current = queue.popleft()                current = queue.popleft()
                for combination in combinations:                for combination in combinations:
                    nr, nc = current[0] + combination[0], current[1] + combination[1]                    nr, nc = current[0] + combination[0], current[1] + combination[1]
                    if (nr<0 or nc<0) or (nr==ROWS or nc==COLS) or (grid[nr][nc]!=1):                    if (nr<0 or nc<0) or (nr==ROWS or nc==COLS) or (grid[nr][nc]!=1):
                        continue                        continue
                    queue.append([nr, nc])                    queue.append([nr, nc])
                    grid[nr][nc] = 2                    grid[nr][nc] = 2
                    fresh -= 1                    fresh -= 1
            time += 1            time += 1
        return time if fresh==0 else -1        return time if fresh==0 else -1
