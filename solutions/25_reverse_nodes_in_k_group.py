# Problem: Reverse Nodes in k-Group
# Number: 25
# Difficulty: Hard
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                curr.next = prev                curr.next = prev
                prev = curr                prev = curr
                curr = tmp                curr = tmp

            tmp = groupPrev.next            tmp = groupPrev.next
            groupPrev.next = kth            groupPrev.next = kth
            groupPrev = tmp            groupPrev = tmp
        return dummy.next        return dummy.next

    def getKth(self, curr, k):    def getKth(self, curr, k):
        while curr and k > 0:        while curr and k > 0:
            curr = curr.next            curr = curr.next
            k -= 1            k -= 1
        return curr        return curr
