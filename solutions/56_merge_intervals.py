# Problem: Merge Intervals
# Number: 56
# Difficulty: Medium
# URL: https://leetcode.com/problems/merge-intervals/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start<=lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
            # [1, 5], [2, 4] Take note of this edge case
        return output
