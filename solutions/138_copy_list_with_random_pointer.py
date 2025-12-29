# Problem: Copy List with Random Pointer
# Number: 138
# Difficulty: Medium
# URL: https://leetcode.com/problems/copy-list-with-random-pointer/
# Submission Status: Accepted
# Runtime: 37 ms
# Memory: N/A

        store = {None: None}        store = {None: None}
        curr = head        curr = head
        while (curr):        while (curr):
            temp = Node(curr.val)            temp = Node(curr.val)
            store[curr] = temp            store[curr] = temp
            curr = curr.next            curr = curr.next
                
        curr = head        curr = head
        while (curr):        while (curr):
            next_node = curr.next            next_node = curr.next
            store[curr].next = store[next_node]            store[curr].next = store[next_node]

            random_node = curr.random            random_node = curr.random
            store[curr].random = store[random_node]            store[curr].random = store[random_node]

            curr = curr.next            curr = curr.next
        return store[head]        return store[head]
