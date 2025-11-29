# Problem: Search in a Binary Search Tree
# Number: 700
# Difficulty: Easy
# URL: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
