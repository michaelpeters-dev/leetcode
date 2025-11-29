# Problem: Print Binary Tree
# Number: 655
# Difficulty: Medium
# URL: https://leetcode.com/problems/print-binary-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        rows = height(root)
        cols = (2**rows)-1

        res = [["" for c in range(cols)] for r in range(rows)]

        def dfs(node, row, left, right):
            if not node:
                return
            mid = (left + right)//2
            res[row][mid] = str(node.val)

            dfs(node.left, row+1, left, mid-1)
            dfs(node.right, row+1, mid+1, right)
        dfs(root, 0, 0, cols-1)
        return res
