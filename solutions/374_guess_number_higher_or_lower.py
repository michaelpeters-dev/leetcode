# Problem: Guess Number Higher or Lower
# Number: 374
# Difficulty: Easy
# URL: https://leetcode.com/problems/guess-number-higher-or-lower/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n
        while low<=high:
            mid = (low+high)//2

            if guess(mid)<0:
                high = mid-1
            elif guess(mid)>0:
                low=mid+1
            else:
                return mid
