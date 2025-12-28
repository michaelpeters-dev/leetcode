# Problem: Gas Station
# Number: 134
# Difficulty: Medium
# URL: https://leetcode.com/problems/gas-station/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):        if sum(gas) < sum(cost):
            return -1            return -1

        total = 0        total = 0
        start = 0        start = 0
        for i in range(len(gas)):        for i in range(len(gas)):
            total += (gas[i] - cost[i])            total += (gas[i] - cost[i])

            if total<0:            if total<0:
                total = 0                total = 0
                start = i + 1                start = i + 1
        return start        return start

