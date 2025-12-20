# Problem: Search a 2D Matrix
# Number: 74
# Difficulty: Medium
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A


        l, r = 0, (m * n - 1)        l, r = 0, (m * n - 1)

        while l<=r:        while l<=r:
            mid = (l + r)//2            mid = (l + r)//2

            left_coord = matrix[l//n][l%n]            left_coord = matrix[l//n][l%n]
            right_cord = matrix[r//n][r%n]            right_cord = matrix[r//n][r%n]
            mid_coord = matrix[mid//n][mid%n]            mid_coord = matrix[mid//n][mid%n]

            if mid_coord==target:            if mid_coord==target:
                return True                return True
            elif mid_coord>target:            elif mid_coord>target:
                r = mid - 1                r = mid - 1
            else:            else:
                l = mid + 1                l = mid + 1
        return False        return False
