# Problem: Course Schedule
# Number: 207
# Difficulty: Medium
# URL: https://leetcode.com/problems/course-schedule/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for i in range(numCourses): # Map each course to a prereq list
            premap[i] = []

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visitSet = set() # All courses along the curr dfs path
        def dfs(course):
            if course in visitSet:
                return False
            if premap[course]==[]:
                return True

            visitSet.add(course)
            for pre in premap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)
            premap[course] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
