# Problem: Maximum Depth of Binary Tree
# Number: 104
# Difficulty: Easy
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))
