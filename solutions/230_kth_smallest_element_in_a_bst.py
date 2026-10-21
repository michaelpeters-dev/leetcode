# Problem:    230. Kth Smallest Element in a BST
# Difficulty: Medium
# Language:   Python3
# Runtime:    3 ms
# Memory:     21.9 MB
# Solved:     2026-10-21
# URL:        https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        counter = [0]
        result = [0]

        def inOrder(node):
            if (node == None):
                return

            if (node.left):
                inOrder(node.left)
            
            counter[0] += 1
            if (counter[0] == k):
                result[0] = node.val

            if (node.right):
                inOrder(node.right)

        inOrder(root)
        return result[0]
