# Problem: Valid Sudoku
# Number: 36
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                for j in range(c, c + 3):                for j in range(c, c + 3):
                    if board[i][j]==".":                    if board[i][j]==".":
                        continue                        continue
                    if board[i][j] not in nums:                    if board[i][j] not in nums:
                        nums.add(board[i][j])                        nums.add(board[i][j])
                        continue                        continue
                    return False                    return False
            return True            return True
                
        for r in range(0, 9, 3):        for r in range(0, 9, 3):
            for c in range(0, 8, 3):            for c in range(0, 8, 3):
                if not checkSubsquare(r, c):                if not checkSubsquare(r, c):
            for i in range(r, r + 3):            for i in range(r, r + 3):
            nums = set()            nums = set()
        def checkSubsquare(r, c):        def checkSubsquare(r, c):

                    return False                    return False
        return True        return True
