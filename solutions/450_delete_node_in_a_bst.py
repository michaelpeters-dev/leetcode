# Problem: Delete Node in a BST
# Number: 450
# Difficulty: Medium
# URL: https://leetcode.com/problems/delete-node-in-a-bst/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur.val

        if not root:
            return None

        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            minval = findMin(root.right)
            root.val = minval
            root.right = self.deleteNode(root.right, minval)
        return root
