# Problem: Merge Two Sorted Lists
# Number: 21
# Difficulty: Easy
# URL: https://leetcode.com/problems/merge-two-sorted-lists/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
        return dummy.next
