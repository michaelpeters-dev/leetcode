# Problem: Course Schedule II
# Number: 210
# Difficulty: Medium
# URL: https://leetcode.com/problems/course-schedule-ii/
# Submission Status: Accepted
# Runtime: 8 ms
# Memory: 21.60 MB

        # visited -> crs has been added to output        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added to cycle        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle        # unvisited -> crs not added to output or cycle

        output = []        output = []
        visit, cycle = set(), set()        visit, cycle = set(), set()
        def dfs(crs):        def dfs(crs):
            if crs in cycle:            if crs in cycle:
                return False                return False
            if crs in visit:            if crs in visit:
                return True                return True
                        
            cycle.add(crs)            cycle.add(crs)
            for pre in prereq[crs]:            for pre in prereq[crs]:
                if dfs(pre) == False:                if dfs(pre) == False:
                    return False                    return False
            cycle.remove(crs)            cycle.remove(crs)
                
        # a course has 3 pos states        # a course has 3 pos states
                
            visit.add(crs)            visit.add(crs)
            output.append(crs)            output.append(crs)
            return True            return True

        for c in range(numCourses):        for c in range(numCourses):
            if dfs(c) == False:            if dfs(c) == False:
