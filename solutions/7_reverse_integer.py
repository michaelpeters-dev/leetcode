# Problem: Reverse Integer
# Number: 7
# Difficulty: Medium
# URL: https://leetcode.com/problems/reverse-integer/
# Submission Status: Accepted
# Runtime: 38 ms
# Memory: N/A

        MIN = -1 * 2**31        MIN = -1 * 2**31
        print(MAX)        print(MAX)
        print(MIN)        print(MIN)

        while x:        while x:
        return res        return res
            digit = int(math.fmod(x, 10))            digit = int(math.fmod(x, 10))
        res = 0         res = 0 
            x = int(x/10)            x = int(x/10)
            if (res > MAX // 10 or (res==MAX//10 and digit >= MAX%10)):            if (res > MAX // 10 or (res==MAX//10 and digit >= MAX%10)):
                return 0                return 0
            if (res < MIN // 10 or (res==MIN//10 and digit <= MIN%10)):            if (res < MIN // 10 or (res==MIN//10 and digit <= MIN%10)):
                return 0                return 0
            res = (res * 10) + digit            res = (res * 10) + digit

        MAX = 2**31 - 1        MAX = 2**31 - 1
    def reverse(self, x: int) -> int:    def reverse(self, x: int) -> int:
class Solution:class Solution:
