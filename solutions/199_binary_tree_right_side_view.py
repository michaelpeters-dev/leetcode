# Problem: Binary Tree Right Side View
# Number: 199
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-right-side-view/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            return []            return []

        queue = deque([root])         queue = deque([root]) 
        res = []        res = []

        while queue:        while queue:
            for i in range(len(queue)):            for i in range(len(queue)):
                if i==length-1:                if i==length-1:
                    res.append(node.val)                    res.append(node.val)
                if node.left: queue.append(node.left)                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)                if node.right: queue.append(node.right)
        return res        return res
                node = queue.popleft()                node = queue.popleft()
            length = len(queue)            length = len(queue)
