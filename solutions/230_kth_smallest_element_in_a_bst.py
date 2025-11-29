# Problem: Kth Smallest Element in a BST
# Number: 230
# Difficulty: Medium
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur, stack = root, []
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n==k:
                return cur.val
            cur = cur.right
