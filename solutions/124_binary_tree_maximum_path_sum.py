# Problem: Binary Tree Maximum Path Sum
# Number: 124
# Difficulty: Hard
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]
