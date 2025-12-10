# Problem: Count Good Nodes in Binary Tree
# Number: 1448
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Submission Status: Accepted
# Runtime: 48 ms
# Memory: N/A

# class TreeNode:# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):#     def __init__(self, val=0, left=None, right=None):
#         self.val = val#         self.val = val
#         self.left = left#         self.left = left
#         self.right = right#         self.right = right
class Solution:class Solution:
    def goodNodes(self, root: TreeNode) -> int:    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):        def dfs(node, maxVal):
            if not node:            if not node:
                return 0                return 0
            res = 1 if node.val >= maxVal else 0            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)            res += dfs(node.right, maxVal)
            return res            return res
        return dfs(root, root.val)        return dfs(root, root.val)

