# Problem: Median of Two Sorted Arrays
# Number: 4
# Difficulty: Hard
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            j = half - i - 2 #B            j = half - i - 2 #B

            Aleft = A[i] if i >= 0 else float("-inf")            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i+1) < len(A) else float("inf")            Aright = A[i + 1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:            if Aleft <= Bright and Bleft <= Aright:
            # partition is correct            # partition is correct
                # odd                # odd
                if total % 2:                if total % 2:
                    return min(Aright, Bright)                    return min(Aright, Bright)
                else:                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:            elif Aleft > Bright:
                r = i - 1                r = i - 1
            else:            else:
            i = (l + r) // 2 #A            i = (l + r) // 2 #A
        while True:        while True:
