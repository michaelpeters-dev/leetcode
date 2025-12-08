# Problem: Median of Two Sorted Arrays
# Number: 4
# Difficulty: Hard
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 17.94 MB

            ALeft = A[i] if i>=0 else float("-inf")            ALeft = A[i] if i>=0 else float("-inf")
            ARight = A[i + 1] if i + 1 < len(A) else float("inf")            ARight = A[i + 1] if i + 1 < len(A) else float("inf")
            BLeft = B[j] if j>=0 else float("-inf")            BLeft = B[j] if j>=0 else float("-inf")
            BRight = B[j + 1] if j + 1 < len(B) else float("inf")            BRight = B[j + 1] if j + 1 < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight:            if ALeft <= BRight and BLeft <= ARight:
                if total%2==0:                if total%2==0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            # Calculate the lower and upper bounds of each array            # Calculate the lower and upper bounds of each array

                return min(ARight, BRight)                return min(ARight, BRight)
            elif ALeft > BRight:            elif ALeft > BRight:
                r -= 1                r -= 1
            else:            else:
                l += 1                l += 1
                        
