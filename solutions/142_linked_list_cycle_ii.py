# Problem: Linked List Cycle II
# Number: 142
# Difficulty: Medium
# URL: https://leetcode.com/problems/linked-list-cycle-ii/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head

        while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast==slow:
                    slow2 = head
                    while slow != slow2:
                        slow = slow.next
                        slow2 = slow2.next
                    return slow
        return None
