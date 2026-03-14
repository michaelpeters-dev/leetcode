# Problem: Valid Sudoku
# Number: 36
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
# Submission Status: Accepted
# Runtime: 11 ms
# Memory: 12.50 MB

        """        """
        :type board: List[List[str]]        :type board: List[List[str]]
        :rtype: bool        :rtype: bool
        """        """
        row = {i: set() for i in range(9)}        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}        col = {i: set() for i in range(9)}
        box = {(i, j): set() for i in range(3) for j in range(3)}        box = {(i, j): set() for i in range(3) for j in range(3)}

        for rowcount in range(9):        for rowcount in range(9):
            for colcount in range(9):            for colcount in range(9):
                num = board[rowcount][colcount]                num = board[rowcount][colcount]
                row[rowcount].add(num)                row[rowcount].add(num)
                col[colcount].add(num)                col[colcount].add(num)
                box[(rowcount//3, colcount//3)].add(num)                box[(rowcount//3, colcount//3)].add(num)
                if num in row[rowcount] or num in col[colcount] or num in box[(rowcount//3, colcount//3)]:                if num in row[rowcount] or num in col[colcount] or num in box[(rowcount//3, colcount//3)]:
                    return False                    return False

                if num==".":                if num==".":
                    continue                    continue
        return True        return True
