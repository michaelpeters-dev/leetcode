# Problem: Valid Sudoku
# Number: 36
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                    continue                    continue

                if (val in horizontal.get(i, set())                if (val in horizontal.get(i, set())
                    or val in vertical.get(j, set())                    or val in vertical.get(j, set())
                    or val in block.get(square, set())):                    or val in block.get(square, set())):
                    return False                    return False
                else:                else:
                                
        return True        return True
                if val==".":                if val==".":
                square = (i//3, j//3)                square = (i//3, j//3)

                val = board[i][j]                val = board[i][j]

            for j in range(0, 9):            for j in range(0, 9):
        for i in range(0, 9):        for i in range(0, 9):

        block = {}        block = {}
        vertical = {}        vertical = {}
        horizontal = {}        horizontal = {}

        """        """
                    horizontal.setdefault(i, set()).add(val)                    horizontal.setdefault(i, set()).add(val)
        :rtype: bool        :rtype: bool
                    vertical.setdefault(j, set()).add(val)                    vertical.setdefault(j, set()).add(val)
                    block.setdefault(square, set()).add(val)                    block.setdefault(square, set()).add(val)
                                
