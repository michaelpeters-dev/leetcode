# Problem: Linked List Cycle
# Number: 141
# Difficulty: Easy
# URL: https://leetcode.com/problems/linked-list-cycle/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        L = head
        R = head
        while R and R.next:
            L = L.next
            R = R.next.next
            if R==L:
                return True
        return False
