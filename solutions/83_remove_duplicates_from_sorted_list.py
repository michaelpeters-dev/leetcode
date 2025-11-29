# Problem: Remove Duplicates from Sorted List
# Number: 83
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val==current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
