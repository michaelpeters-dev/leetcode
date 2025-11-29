# Problem: Remove Linked List Elements
# Number: 203
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-linked-list-elements/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next  # skip the node
            else:
                current = current.next

        return dummy.next
