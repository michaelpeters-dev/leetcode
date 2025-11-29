# Problem: Non-overlapping Intervals
# Number: 435
# Difficulty: Medium
# URL: https://leetcode.com/problems/non-overlapping-intervals/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
