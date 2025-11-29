# Problem: Binary Tree Inorder Traversal
# Number: 94
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def inorderTraversal(self, root):
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res
