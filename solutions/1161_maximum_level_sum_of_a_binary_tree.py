# Problem: Maximum Level Sum of a Binary Tree
# Number: 1161
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Submission Status: Accepted
# Runtime: 19 ms
# Memory: 23.00 MB

            for i in range(len(queue)):            for i in range(len(queue)):
        maximum = [float("-inf"), level]        maximum = [float("-inf"), level]
            counter = 0            counter = 0
                popped = queue.popleft()                popped = queue.popleft()
                counter += popped.val                 counter += popped.val 
                if popped.left: queue.append(popped.left)                if popped.left: queue.append(popped.left)
                if popped.right: queue.append(popped.right)                if popped.right: queue.append(popped.right)
        return maximum[1]        return maximum[1]
            if counter>maximum[0]:            if counter>maximum[0]:
                maximum[0] = counter                maximum[0] = counter
                maximum[1] = level                maximum[1] = level
        while queue:        while queue:
            level += 1            level += 1


