# Problem: Middle of the Linked List
# Number: 876
# Difficulty: Easy
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def middleNode(self, head):
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
