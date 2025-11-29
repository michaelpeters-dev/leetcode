# Problem: Binary Tree Level Order Traversal
# Number: 102
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
