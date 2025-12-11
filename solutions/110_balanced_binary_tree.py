# Problem: Balanced Binary Tree
# Number: 110
# Difficulty: Easy
# URL: https://leetcode.com/problems/balanced-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution:class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):        def dfs(node):
            if not node:            if not node:
                return 0                return 0

            left_height = 1 + dfs(node.left)            left_height = 1 + dfs(node.left)
            right_height = 1 + dfs(node.right)            right_height = 1 + dfs(node.right)
        trace = [True]        trace = [True]
                        
            if abs(left_height - right_height) > 1:            if abs(left_height - right_height) > 1:
                trace[0] = False                trace[0] = False
                        
            return max(left_height, right_height)            return max(left_height, right_height)
        dfs(root)        dfs(root)
        return trace[0]        return trace[0]
