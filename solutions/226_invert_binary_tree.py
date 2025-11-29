# Problem: Invert Binary Tree
# Number: 226
# Difficulty: Easy
# URL: https://leetcode.com/problems/invert-binary-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
