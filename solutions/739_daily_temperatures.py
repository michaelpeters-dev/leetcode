# Problem: Daily Temperatures
# Number: 739
# Difficulty: Medium
# URL: https://leetcode.com/problems/daily-temperatures/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []        stack = []
        res = [0] * len(temperatures)        res = [0] * len(temperatures)

        for i in range(len(temperatures)):        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()                prev = stack.pop()
                res[prev] = i - prev                res[prev] = i - prev
            stack.append(i)            stack.append(i)
        return res        return res
