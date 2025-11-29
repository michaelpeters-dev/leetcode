# Problem: Remove Nth Node From End of List
# Number: 19
# Difficulty: Medium
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
