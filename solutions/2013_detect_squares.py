# Problem: Detect Squares
# Number: 2013
# Difficulty: Medium
# URL: https://leetcode.com/problems/detect-squares/
# Submission Status: Accepted
# Runtime: 263 ms
# Memory: 19.19 MB


    def __init__(self):    def __init__(self):
    def add(self, point: List[int]) -> None:    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1        self.ptsCount[tuple(point)] += 1
        self.ptsCount = defaultdict(int)        self.ptsCount = defaultdict(int)

    def count(self, point: List[int]) -> int:    def count(self, point: List[int]) -> int:
        res = 0        res = 0
                
        px, py = point        px, py = point
        for x, y in self.pts:        for x, y in self.pts:
            if (abs(py - y) != abs(px - x) or x == px or y == py):            if (abs(py - y) != abs(px - x) or x == px or y == py):
                continue                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]             res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] 
        return res        return res
        self.pts = []        self.pts = []
        self.pts.append(point)        self.pts.append(point)
                
