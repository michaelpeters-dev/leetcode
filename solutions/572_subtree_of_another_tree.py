# Problem: Subtree of Another Tree
# Number: 572
# Difficulty: Easy
# URL: https://leetcode.com/problems/subtree-of-another-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root and subRoot: return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
        return False
