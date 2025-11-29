# Problem: Palindrome Linked List
# Number: 234
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome-linked-list/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current = slow
        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        # prev is the head of the reversed second half
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
