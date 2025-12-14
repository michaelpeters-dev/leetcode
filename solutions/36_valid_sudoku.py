# Problem: Valid Sudoku
# Number: 36
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):        for r in range(9):
            for c in range(9):            for c in range(9):
                if board[r][c]==".":                if board[r][c]==".":
                    continue                    continue
                if (board[r][c] in rows[r] or                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):                    board[r][c] in squares[(r//3, c//3)]):
                    return False                    return False
                rows[r].add(board[r][c])                rows[r].add(board[r][c])
                cols[c].add(board[r][c])                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])                squares[(r//3, c//3)].add(board[r][c])
        return True        return True
