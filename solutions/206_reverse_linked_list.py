# Problem: Reverse Linked List
# Number: 206
# Difficulty: Easy
# URL: https://leetcode.com/problems/reverse-linked-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None
        while curr:
            store = curr.next
            curr.next = prev
            prev = curr
            curr = store
        return prev
