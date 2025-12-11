# Problem: Balanced Binary Tree
# Number: 110
# Difficulty: Easy
# URL: https://leetcode.com/problems/balanced-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            if not node:            if not node:
                return 0                return 0

            left = dfs(node.left)            left = dfs(node.left)
            if left == -1:            if left == -1:
                return -1                return -1
                        
            right = dfs(node.right)            right = dfs(node.right)
            if right == -1:            if right == -1:
                return -1                return -1
                        
            if abs(left - right) > 1:            if abs(left - right) > 1:
                return -1                return -1
                        
            return 1 + max(left, right)            return 1 + max(left, right)
        return dfs(root) != -1        return dfs(root) != -1
