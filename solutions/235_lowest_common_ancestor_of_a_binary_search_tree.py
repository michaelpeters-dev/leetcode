# Problem: Lowest Common Ancestor of a Binary Search Tree
# Number: 235
# Difficulty: Medium
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val < root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
