# Problem: Counting Bits
# Number: 338
# Difficulty: Easy
# URL: https://leetcode.com/problems/counting-bits/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n+1):
            ans.append(self.counter(i))
        return ans

    # Helper Function
    def counter(self, n):
        binary_string = str(bin(n))
        count = 0
        for b in binary_string:
            if b=="1":
                count += 1
        return count
