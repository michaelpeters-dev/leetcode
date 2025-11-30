# Problem: Zigzag Conversion
# Number: 6
# Difficulty: Medium
# URL: https://leetcode.com/problems/zigzag-conversion/
# Submission Status: Accepted
# Runtime: 498 ms
# Memory: 24.66 MB

                i += 1                i += 1
                row -= 1                row -= 1
                col += 1                col += 1

            # Move to the next downward start            # Move to the next downward start
            row += 2            row += 2
            col -= 1            col -= 1

        # Build the String        # Build the String
        temp = ""        temp = ""
        for r in range(len(res)):        for r in range(len(res)):
            for c in range(len(res[0])):            for c in range(len(res[0])):
                if res[r][c]:                if res[r][c]:
                    temp += res[r][c]                    temp += res[r][c]
        return temp        return temp
