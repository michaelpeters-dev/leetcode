# Problem: Diameter of Binary Tree
# Number: 543
# Difficulty: Easy
# URL: https://leetcode.com/problems/diameter-of-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

#         self.val = val#         self.val = val
#         self.left = left#         self.left = left
#         self.right = right#         self.right = right
class Solution:class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = [0]        maximum = [0]
        def dfs(root):        def dfs(root):
            if not root:            if not root:
                return 0                return 0
            max_left_branch = dfs(root.left)            max_left_branch = dfs(root.left)
            max_right_branch = dfs(root.right)            max_right_branch = dfs(root.right)
                        
            curr_diameter = max_left_branch + max_right_branch            curr_diameter = max_left_branch + max_right_branch
            maximum[0] = max(maximum[0], curr_diameter)            maximum[0] = max(maximum[0], curr_diameter)
            return 1 + max(max_left_branch, max_right_branch)            return 1 + max(max_left_branch, max_right_branch)
        dfs(root)        dfs(root)
        return maximum[0]        return maximum[0]
