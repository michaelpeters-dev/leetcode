# Problem: Valid Parenthesis String
# Number: 678
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-parenthesis-string/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.06 MB


        for c in s:        for c in s:
            if c=="(":            if c=="(":
                leftMin, leftMax = leftMin  +1, leftMax + 1                leftMin, leftMax = leftMin  +1, leftMax + 1
            elif c == ")":            elif c == ")":
                leftMin, leftMax = leftMin  - 1, leftMax - 1                leftMin, leftMax = leftMin  - 1, leftMax - 1
            else:            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:            if leftMax < 0:
                return False                return False
            if leftMin < 0:            if leftMin < 0:
                leftMin = 0                leftMin = 0
        leftMin, leftMax = 0, 0        leftMin, leftMax = 0, 0
        return leftMin==0        return leftMin==0
