# Problem: Surrounded Regions
# Number: 130
# Difficulty: Medium
# URL: https://leetcode.com/problems/surrounded-regions/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        for r in range(ROWS):        for r in range(ROWS):
        # 1. Capture the unsurrounded regions (O -> T), only DFS        # 1. Capture the unsurrounded regions (O -> T), only DFS

            for c in range(COLS):            for c in range(COLS):
                if board[r][c]=="O" and (r in [0, ROWS-1] or c in [0, COLS - 1]):                if board[r][c]=="O" and (r in [0, ROWS-1] or c in [0, COLS - 1]):
                    capture(r, c)                    capture(r, c)
            capture(r, c - 1)            capture(r, c - 1)
            capture(r, c + 1)            capture(r, c + 1)
            capture(r - 1, c)            capture(r - 1, c)
            capture(r + 1, c)            capture(r + 1, c)
            board[r][c] = "T"            board[r][c] = "T"
                return                return
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":
        def capture(r, c):        def capture(r, c):

        ROWS, COLS = len(board), len(board[0])        ROWS, COLS = len(board), len(board[0])
        """        """
        Do not return anything, modify board in-place instead.        Do not return anything, modify board in-place instead.
