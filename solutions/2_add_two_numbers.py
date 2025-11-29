# Problem: Add Two Numbers
# Number: 2
# Difficulty: Medium
# URL: https://leetcode.com/problems/add-two-numbers/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 18.00 MB

        while l1 or l2 or carry:        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry            val = v1 + v2 + carry
            carry = val // 10            carry = val // 10
            val = val % 10            val = val % 10

            curr.next = ListNode(val)            curr.next = ListNode(val)
            curr = curr.next            curr = curr.next

            if l1:            if l1:
                l1 = l1.next                l1 = l1.next
            if l2:            if l2:
                l2 = l2.next                l2 = l2.next

        return dummy.next        return dummy.next

