# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Number: 105
# Difficulty: Medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
