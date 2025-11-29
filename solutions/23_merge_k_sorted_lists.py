# Problem: Merge k Sorted Lists
# Number: 23
# Difficulty: Hard
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists or len(lists)==0:
            return None

        while len(lists)>1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            elif l2.val<=l1.val:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next
