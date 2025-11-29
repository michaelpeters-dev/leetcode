# Problem: Number of Students Unable to Eat Lunch
# Number: 1700
# Difficulty: Easy
# URL: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                return res

        return res
