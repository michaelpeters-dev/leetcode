# Problem: Delete Node in a Linked List
# Number: 237
# Difficulty: Medium
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
