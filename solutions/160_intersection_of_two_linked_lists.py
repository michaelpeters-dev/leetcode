# Problem: Intersection of Two Linked Lists
# Number: 160
# Difficulty: Easy
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lengthA = 0
        lengthB = 0

        currentA = headA
        currentB = headB

        while currentA:
            lengthA += 1
            currentA = currentA.next
        while currentB:
            lengthB += 1
            currentB = currentB.next

        if lengthA > lengthB:
            for i in range(lengthA - lengthB):
                headA = headA.next

        else:
            for i in range(lengthB - lengthA):
                headB = headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
