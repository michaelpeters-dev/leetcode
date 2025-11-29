# Problem: Spiral Matrix
# Number: 54
# Difficulty: Medium
# URL: https://leetcode.com/problems/spiral-matrix/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O (m * n), O(1)
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left<right and top<bottom:
            # Get every value in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Get every value in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # Get every value in the bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # Get every value in the left col
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
