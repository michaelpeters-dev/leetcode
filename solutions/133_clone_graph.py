# Problem: Clone Graph
# Number: 133
# Difficulty: Medium
# URL: https://leetcode.com/problems/clone-graph/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        if node:
            return dfs(node)
        else:
            return None
