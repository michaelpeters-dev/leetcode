# Problem: Insert into a Binary Search Tree
# Number: 701
# Difficulty: Medium
# URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val<root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val>root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root
