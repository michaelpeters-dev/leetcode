# Problem: N-Queens
# Number: 51
# Difficulty: Hard
# URL: https://leetcode.com/problems/n-queens/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                if (c in cols) or (r+c in posDiag) or (r-c in negDiag):                if (c in cols) or (r+c in posDiag) or (r-c in negDiag):
                    continue                    continue
                                
            for c in range(n):            for c in range(n):
                        
                res.append(copy)                 res.append(copy) 
                return                return
            if r==n:            if r==n:
                copy = ["".join(row) for row in board]                copy = ["".join(row) for row in board]
                board[r][c] = "Q"                board[r][c] = "Q"
                cols.add(c)                cols.add(c)
                posDiag.add(r + c)                posDiag.add(r + c)
                negDiag.add(r - c)                negDiag.add(r - c)

                backtrack(r + 1)                backtrack(r + 1)

                board[r][c] = "."                board[r][c] = "."
                cols.remove(c)                cols.remove(c)
                posDiag.remove(r + c)                posDiag.remove(r + c)
