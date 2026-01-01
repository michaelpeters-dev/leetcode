# Problem: Min Stack
# Number: 155
# Difficulty: Medium
# URL: https://leetcode.com/problems/min-stack/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

    def pop(self) -> None:    def pop(self) -> None:
        if self.stack[-1]<=self.minimum[-1]:        if self.stack[-1]<=self.minimum[-1]:
            self.stack.pop()            self.stack.pop()
            self.minimum.pop()            self.minimum.pop()

        self.stack.append(val)        self.stack.append(val)
        if len(self.minimum)==0 or val<=self.minimum[-1]:        if len(self.minimum)==0 or val<=self.minimum[-1]:
            self.minimum.append(val)            self.minimum.append(val)
    def push(self, val: int) -> None:    def push(self, val: int) -> None:

        self.skips = 0        self.skips = 0
        self.stack = []        self.stack = []
        self.minimum = []        self.minimum = []
    def __init__(self):    def __init__(self):

class MinStack:class MinStack:
